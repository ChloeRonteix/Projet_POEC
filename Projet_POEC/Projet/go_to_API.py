'''
Created on 23 janv. 2020

@author: Administrateur
'''
curl -X POST -F data=@mycsvfile.csv -F columns='numeroVoieEtablissement' columns='typeVoieEtablissement' columns='libelleVoieEtablissement',
                                    'codePostalEtablissement', 'libelleCommuneEtablissement' -F columns=postcode -F result_columns=result_id 
https://api-adresse.data.gouv.fr/search/csv/




