'''
Created on 22 janv. 2020

@author: Administrateur
'''
import pandas as pd
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)
import numpy as np

df=pd.read_csv('StockEtablissement_utf8.csv', nrows=150)
print(df.shape)

#print(df.head(10))
print(df.columns)
