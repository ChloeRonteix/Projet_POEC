'''
Created on 23 janv. 2020

@author: Administrateur
'''
import requests

files = {
    'data': (open('mycsvfile.csv', 'rb').read())
    }

data = {'columns': ('numeroVoieEtablissement',
                     'typeVoieEtablissement',
                      'libelleVoieEtablissement',
                       'libelleCommuneEtablissement'),
        'result_columns': ('latitude','longitude'),
        'postcode': 'codePostalEtablissement'
}

res = requests.post('https://api-adresse.data.gouv.fr/search/csv/', files=files, data=data)
print(res.text)




