'''
Created on 23 janv. 2020

@author: Administrateur
'''
from elasticsearch import Elasticsearch
from connect_elastic import es
from read_prepare_csv_SIRENE import df5

es.indices.delete(index='test')

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
                    'latitude': {'type': 'geo_point'},
                    'longitude': {'type': 'geo_point'}
                    }}
}

es.indices.create(index='test', body= request_body)


#creation du dictionnaire a envoyer vers elastic
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

