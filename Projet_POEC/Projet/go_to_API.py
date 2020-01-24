'''
Created on 23 janv. 2020

@author: Administrateur
'''
import requests
import pandas as pd
from io import StringIO


files = {
    'data': (open('mycsvfile.csv', 'rb').read())
    }
'''
'columns': ('numeroVoieEtablissement',
                     'typeVoieEtablissement',
                      'libelleVoieEtablissement',
                       'libelleCommuneEtablissement'),'''

data = {
        'postcode': 'codePostalEtablissement',
        'result_columns': ('latitude','longitude')
        
}
'''
data = {
'data': (open('mycsvfile.csv', 'rb').read()),
       'columns': ('numeroVoieEtablissement',
                    'typeVoieEtablissement',
                     'libelleVoieEtablissement',
                      'libelleCommuneEtablissement',
  'codePostalEtablissement'),
       'result_columns': ('id', 'latitude','longitude')
}'''

res = requests.post('https://api-adresse.data.gouv.fr/search/csv/', files=files, data=data)
print(res.text)


#traitement en dataframe de la réponse de l'API
res_api = res.text
print(res_api)
df = pd.read_csv(StringIO(res_api), header=0)
print(df)
df2 = df[['id', 'latitude', 'longitude']]
print(df2.head())
