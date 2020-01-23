'''
Created on 23 janv. 2020

@author: Administrateur
'''

from Projet import connect_elastic
from Projet import put_csv_elastic
from connect_elastic import es
import csv

# this returns up to 500 rows, adjust to your needs
res = es.search(index="YourIndexName", body={"query": {"match": {"title": "elasticsearch"}}},500)
sample = res['hits']['hits']

#Deuxieme exemple

# Replace the following Query with your own Elastic Search Query
res = es.search(index="search", body=
                {
                    "_source": ["DTDT", "TRDT", "SPLE", "RPLE"],
                    "query": {
                        "bool": {
                            "should": [
                                {"wildcard": {"CN": "TEST1"}}

                            ]
                        }
                    }
}, size=10)


with open('mycsvfile.csv', 'w') as f:  # Just use 'w' mode in 3.x
    header_present  = False
    for doc in res['hits']['hits']:
        my_dict = doc['_source'] 
        if not header_present:
            w = csv.DictWriter(f, my_dict.keys())
            w.writeheader()
            header_present = True


        w.writerow(my_dict)
