'''
Created on 23 janv. 2020

@author: Administrateur
'''
from Projet import connect_elastic
from connect_elastic import es


res = es.search(index="test", body={ "_source" : [
                                    'siret','numeroVoieEtablissement',
                                    'typeVoieEtablissement', 'libelleVoieEtablissement',
                                    'codePostalEtablissement', 'libelleCommuneEtablissement'], 
                                    "query": { "bool": { "must_not": { "exists": { "field": "location" }}}}}, size=5)
print(res)