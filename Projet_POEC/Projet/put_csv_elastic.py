'''
Created on 23 janv. 2020

@author: Administrateur
'''
from elasticsearch import Elasticsearch
from Projet import connect_elastic
from connect_elastic import *
from Projet import read_prepare_csv_SIRENE
from read_prepare_csv_SIRENE import df5
'''
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
#es.indices.delete(index='test')
'''
#creation du distionnaire a envoyer vers elastic
bulk_data = []
for idx, row in df5.iterrows():
        data_dict = {}
        for i in range(len(row)):
            data_dict[df5.columns[i]] = str(row[i])
            op_dict = {
            "index": {
                "_index": "test",
                "_type": "_doc"
            }
        }
        bulk_data.append(op_dict)
        bulk_data.append(data_dict)
print(bulk_data)

#envoi des donnees vers elastic
es.bulk(index='test', body=bulk_data)

