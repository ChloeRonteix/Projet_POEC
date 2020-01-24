'''
Created on 23 janv. 2020

@author: Administrateur
'''
from elasticsearch import Elasticsearch
from connect_elastic import es
from read_prepare_csv import df5


#creation du dictionnaire a envoyer vers elastic
bulk_data = []
for idx, row in df5.iterrows():
    data_dict = {}
    for i in range(len(row)):
        data_dict[df5.columns[i]] = str(row[i])
        op_dict = {
            "index": {
            "_index": "test2",
            "_type": "_doc"
            }
        }
        bulk_data.append(op_dict)
        bulk_data.append(data_dict)
#print(bulk_data)

#envoi des donnees vers elastic
es.bulk(index='test2', body=bulk_data)

