'''
Created on 23 janv. 2020

@author: Administrateur
'''

from connect_elastic import es
import csv

# recherche elastic visee
res = es.search(index="test", body={ "_source" : [
                                    'siret','numeroVoieEtablissement',
                                    'typeVoieEtablissement', 'libelleVoieEtablissement',
                                    'codePostalEtablissement', 'libelleCommuneEtablissement'], 
                                    "query": { "bool": { "must_not": { "exists": { "field": "coordonnees" }}}}}, size=5)
sample = res['hits']['hits']

with open('mycsvfile.csv', 'w') as csvfile:
    header_present = False
    for doc in sample: 
        my_dict = doc['_source'] 
        if not header_present:
            w = csv.DictWriter(csvfile, my_dict.keys())
            w.writeheader()
            header_present = True
        w.writerow(my_dict)
