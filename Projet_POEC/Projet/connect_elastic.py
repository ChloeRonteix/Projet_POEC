'''
Created on 22 janv. 2020

@author: Administrateur

connection vers elastic_search
'''

from elasticsearch import Elasticsearch
import certifi
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




