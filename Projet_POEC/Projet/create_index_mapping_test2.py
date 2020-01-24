'''
Created on 24 janv. 2020

@author: Administrateur
'''
from elasticsearch import Elasticsearch
from connect_elastic import es

if es.indices.exists(index='test2'):
    es.indices.delete(index='test2')


request_body = {
        "settings" : {
            "number_of_shards": 3,
            "number_of_replicas": 1
        },
        "settings": {"max_result_window": "100000"},
        'mappings': {
                'properties': {
                    'siret':  {'type': 'long'},
                    'numeroVoieEtablissement':  {'type': 'text'},
                    'typeVoieEtablissement':  {'type': 'text'},
                    'libelleVoieEtablissement':  {'type': 'text'},
                    'codePostalEtablissement':  {'type': 'text'},
                    'libelleCommuneEtablissement':  {'type': 'text'},
                    'location': {'type': 'geo_point'}
                    }}
}

es.indices.create(index='test2', body= request_body)


