'''
Created on 23 janv. 2020

@author: Administrateur
'''
import requests
import pandas as pd
from io import StringIO
from elasticsearch import Elasticsearch
from connect_elastic import es


files = {
    'data': (open('mycsvfile.csv', 'rb').read())
    }

data = {
        'postcode': 'codePostalEtablissement',
        'result_columns': ('longitude','latitude')
        
}
print('Envoie API')
res = requests.post('https://api-adresse.data.gouv.fr/search/csv/', files=files, data=data)
#print(res.text)
print('API finish')

#traitement en dataframe de la réponse de l'API
res_api = res.text
#print(res_api)
df = pd.read_csv(StringIO(res_api), header=0)
#print(df)
df2 = df[['id', 'longitude', 'latitude']]
#print(df2.head())

#update de la base elastic
print('Enrichissement')
for idx, row in df2.iterrows():
    id_et = row['id']
    latitude = row['latitude']
    longitude = row['longitude']
    #print(id_et,longitude,latitude)
    #print(es.update(index='test3', id=id_et, body= {"doc":{"location": [longitude,latitude]}}))
print('Finish process')
