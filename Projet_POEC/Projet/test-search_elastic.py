'''
Created on 23 janv. 2020

@author: Administrateur
'''
from Projet import connect_elastic
from connect_elastic import es

res = es.search(index="test", body={"query": { "bool": { "must_not": { "exists": { "field": "coordonnees" }}}}}, size=5)
print(res)