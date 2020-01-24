'''
Created on 23 janv. 2020

@author: Administrateur
'''

from connect_elastic import es
import csv

# recherche elastic visee
res = es.search(index="test2", body={ "_source" : [
                                    'numeroVoieEtablissement',
                                    'typeVoieEtablissement', 'libelleVoieEtablissement',
                                    'codePostalEtablissement', 'libelleCommuneEtablissement'], 
                                    "query": { "bool": { "must_not": { "exists": { "field": "location" }}}}}, size=15)
sample = res['hits']['hits']

with open('mycsvfile.csv', 'w', newline='') as csvfile:
    header_present = False
    for doc in sample: 
        my_dict = doc['_source']
        my_dict['id'] = doc['_id']
        if not header_present:
            print(my_dict.keys())
            w = csv.DictWriter(csvfile, ['id','numeroVoieEtablissement','typeVoieEtablissement','libelleVoieEtablissement',
                                    'codePostalEtablissement','libelleCommuneEtablissement'])
            w.writeheader()
            header_present = True
        w.writerow(my_dict)
