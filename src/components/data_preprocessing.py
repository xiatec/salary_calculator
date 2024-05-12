import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df_train = pd.read_csv('C:/Users/srija/Documents/DS_Job_Salary_Predictor/data/clean_data.csv')

## Company name
df_train.drop(['company_name'],axis=1,inplace=True)


#Sector
#top_3_labels_sector = [y for y in df_train['Sector'].value_counts().sort_values(ascending=False).head(3).index]
#df_train = df_train[df_train['Sector'].isin(top_3_labels_sector)]
#df_train['Sector'] = df_train['Sector'].apply(lambda i:i.replace(' ','_'))

## Ownership
#top_3_labels_ownership = df_train['Type_of_ownership'].value_counts()
#df_train = df_train[df_train['Type_of_ownership'].isin(top_3_labels_ownership)]
#df_train['Type_of_ownership'] = df_train['Type_of_ownership'].apply(lambda i:i.replace(' ','_'))


##Size
#top_3_labels_size = [y for y in df_train['Size'].value_counts().sort_values(ascending=False).head(3).index]
#df_train = df_train[df_train['Size'].isin(top_3_labels_size)]

## Ownership
#df_train.drop(df_train[df_train['Type_of_ownership']=='Other_Organization'].index,inplace=True)
#df_train.drop(df_train[df_train['Type_of_ownership']=='School_/_School District'].index,inplace=True)
#df_train.drop(df_train[df_train['Type_of_ownership']=='Unknown'].index,inplace=True)

## Industry
#top_3_labels_industry = [y for y in df_train['Industry'].value_counts().sort_values(ascending=False).head(3).index]
#df_train = df_train[df_train['Industry'].isin(top_3_labels_industry)]

dummy_cols = ['Job Title simp','Job Seniority','job_state','job_headquarters','Size','Type of ownership',
              'Industry','Sector','Revenue']
df_dum = pd.get_dummies(df_train[dummy_cols],drop_first=True,dtype=int)

df_train = pd.concat([df_train,df_dum],axis=1)

df_train.drop(['Sector','Size','Type of ownership','Industry','Job Title simp','Job Seniority',
              'job_state','job_headquarters','Revenue'],axis=1,inplace=True)

df_train.to_csv('C:/Users/srija/Documents/DS_Job_Salary_Predictor/data/data_preprocess.csv',index=False)