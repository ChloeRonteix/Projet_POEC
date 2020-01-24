'''
Created on 23 janv. 2020

@author: Administrateur
'''
import requests
import pandas as pd

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

res = requests.post('https://api-adresse.data.gouv.fr/search/csv/', files=files, data=data)
print(res.text)


'''
res_api = res.text
print(res_api)
df = pd.DataFrame(res_api, delimiter=',')
print(df)'''


