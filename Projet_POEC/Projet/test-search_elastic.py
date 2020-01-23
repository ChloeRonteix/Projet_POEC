'''
Created on 23 janv. 2020

@author: Administrateur
'''
from Projet import connect_elastic
from connect_elastic import es

res = es.search(index="test", body={"query": {"bool": { "must": { "match_all": {}}, "filter" : { "coordonnees" : "null"}}}}, size=1)
print(res)