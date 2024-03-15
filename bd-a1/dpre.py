#!/usr/bin/env python
# coding: utf-8



import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from subprocess import run



df = pd.read_csv('wc.csv')
df









df.info()


# # data preprocessing
# ## 1. data cleaning



# checking for null values
df.isnull().sum()




#handling null values for intgers.
for num in df.select_dtypes(include='number').columns: 
    df[num].fillna(df[num].mean(), inplace=True)




# handling null values in Ttitle and Review text features
df.dropna(subset = ['Title','Review Text'], inplace = True)




#handling null values in the rest of object features
for obj in df.select_dtypes(include = 'object').columns:
    df[obj].fillna(df[obj].mode()[0], inplace = True)





# handling outliers if there are any
for x in df.select_dtypes(include='int64').columns:
    IQR = df[x].quantile(0.75) - df[x].quantile(0.25)
    upperfence = df[x].quantile(0.75) + 1.5 * IQR
    lowerfence = df[x].quantile(0.25) - 1.5 * IQR
    outlier = (df[x] < lowerfence) | (df[x] > upperfence)
    df.loc[outlier, x] = df[x].median()
outlier.sum()


# ## 2. data transformation




encoder = LabelEncoder()
df['Labeled Division Name'] = encoder.fit_transform(df['Division Name'])
df['Labeled Department Name'] = encoder.fit_transform(df['Department Name'])
df['Labeled Class Name'] = encoder.fit_transform(df['Class Name'])
df.head()





scaler = StandardScaler()
scaled_data = scaler.fit_transform(df[['Age','Clothing ID']])
scaled_data





df2 = pd.DataFrame(scaled_data)
df2.columns = ['Scaled_Age','Scaled_Clothing ID']
df2


# ## 3. data redution




df.drop(df[['Title','Review Text','Division Name','Department Name','Class Name','Unnamed: 0']],axis=1,inplace=True)
df





df = df.sample(7000)
df





new_df = df.to_csv('res_dpre.csv')

run(["python3", "eda.py", 'res_dpre.csv'])

