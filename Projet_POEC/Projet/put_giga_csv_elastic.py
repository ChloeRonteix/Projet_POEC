'''
Created on 24 janv. 2020

@author: Administrateur
'''
from elasticsearch import Elasticsearch
from read_prepare_big_csv_SIRENE import df5
from connect_elastic import es
from datetime import datetime

compteur = 0
a = {}
for i in range (0,len(df5.index),10000):
    debut = datetime.time.now()
    print('Dictionnaire: batch numero '+ str(i)+' commence a '+ str(debut))
    key=compteur
    a[key]=df5[i:(i+10000)]
    compteur+=1
    fin = datetime.time.now()
    print('termine a '+ str(fin))


debut_envoi = datetime.time.now()
print(debut_envoi)
#creation du dictionnaire a envoyer vers elastic
for key in a:
    debut = datetime.time.now()
    print('Envoi vers Elastic: batch numero '+ str(key)+' commence a '+ str(debut))
    bulk_data = []
    for idx, row in a[key].iterrows():
        data_dict = {}
        for i in range(len(row)):
            data_dict[a[key].columns[i]] = str(row[i])
        op_dict = {
            "index": {
            "_index": "test",
            "_type": "_doc"
            }
        }
        bulk_data.append(op_dict)
        bulk_data.append(data_dict)
        #print(bulk_data)
#envoi des donnees vers elastic
    es.bulk(index='test', body=bulk_data)
    fin = datetime.time.now()
    print('termine a '+ str(fin))
fin_envoi=datetime.time.now()
print('Envoi debute a '+str(debut_envoi))
print('Envoi termine a '+str(fin_envoi))