'''
Created on 22 janv. 2020

@author: Administrateur

connection vers elastic_search
'''

from elasticsearch import Elasticsearch

'''
#connection to Elasticsearch sur le cloud
def connect_to_elastic():
    es = Elasticsearch(['https://9360d0dda6654bbe9684abf43dee7654.eu-central-1.aws.cloud.es.io:9243'])
    return es
'''

#autre methode de connection au cloud
hostUser = "https://9360d0dda6654bbe9684abf43dee7654.eu-central-1.aws.cloud.es.io"
mdpUser = "DESJQtxOrlCVu7m0aEQWyzAU"
es = Elasticsearch([hostUser],http_auth=('elastic', mdpUser),scheme="https",port=9243)
print(es.info())
print(es.ping())

request_body = {
        "settings" : {
            "number_of_shards": 3,
            "number_of_replicas": 1
        },
        "settings": {"max_result_window": "100000"},
        'mappings': {
                'properties': {
                    'siren':  {'type': 'long'},
                    'nic':  {'type': 'integer'},
                    'siret':  {'type': 'long'},
                    'numeroVoieEtablissement':  {'type': 'integer'},
                    'typeVoieEtablissement':  {'type': 'text'},
                    'libelleVoieEtablissement':  {'type': 'text'},
                    'codePostalEtablissement':  {'type': 'integer'},
                    'libelleCommuneEtablissement':  {'type': 'text'},
                    'coordonnees' :{ 'type':'geo_point'}}
                    }}

es.indices.create(index='test', body= request_body)

