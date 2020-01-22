'''
Created on 22 janv. 2020

@author: Administrateur
'''
import pandas as pd
pd.set_option('display.max_columns', 5)
pd.set_option('display.max_rows', 500)
pd.set_option('display.width', 150)
import numpy as np

df=pd.read_csv('StockEtablissement_utf8.csv', nrows=150)
#print('taille de la base: '+ str(df.shape))
print('taille de la base: nombre de lignes = '+ str(df.shape[0]) + ', nombre de colonnes = '+ str(df.shape[1]))

#print(df.head(10))
print()
print('Quelques informations')
print('les colonnes de la bases sont:')
print(str(df.columns))

print()
print('Selection des colonnes pertinentes')
print()
df2 = df[['siret', 'denominationUsuelleEtablissement', 
          'numeroVoieEtablissement',
          'typeVoieEtablissement', 
          'libelleVoieEtablissement',
          'codePostalEtablissement', 
          'libelleCommuneEtablissement', 
          'libelleCommuneEtrangerEtablissement',
          'libellePaysEtrangerEtablissement',
          'trancheEffectifsEtablissement',
          'etatAdministratifEtablissement'
          ]]
print(str(df2.columns))
print()
print('taille de la base: nombres de lignes = '+ str(df2.shape[0]) + ' et nombres de colonnes = '+ str(df2.shape[1]))
print()
print('Garder uniquement les entreprises actives')
print()
df3 = df2[df2.etatAdministratifEtablissement.eq('A')]
print('taille de la base: nombre de lignes = '+ str(df3.shape[0]) + ', nombre de colonnes = '+ str(df3.shape[1]))
print()
print('Supprimer les eventuels doublons')
print()
df4 = df3.drop_duplicates(subset='siret', keep="first")
print('taille de la base: nombre de lignes = '+ str(df4.shape[0]) + ', nombre de colonnes = '+ str(df4.shape[1]))
print()
#print(df4.head(5))
print('Ajout de la colonne coordonnees')
df4['coordonnees']=np.nan
df4['coordonnees']=df4['coordonnees'].astype(object)
print()
print(df4.head(5))
print()
print('Remplacer les valeurs NaN')
values = {'siret' : str(0), 'denominationUsuelleEtablissement' : ' ', 'numeroVoieEtablissement' : str(0),'typeVoieEtablissement' : ' ','libelleVoieEtablissement' : ' ',
       'codePostalEtablissement' : str(0), 'libelleCommuneEtablissement' : ' ', 'libelleCommuneEtrangerEtablissement' : ' ', 'libellePaysEtrangerEtablissement' : ' ',
       'trancheEffectifsEtablissement' : ' ', 'etatAdministratifEtablissement' : ' ', 'coordonnees': str(0)}
df4=df4.fillna(value=values)
print(df4.head(5))
print()
print('ReInitialisation de l\'index')
print()
df5=df4.reset_index(drop=True)
print(df5.head(5))

