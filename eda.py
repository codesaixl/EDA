# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
from matplotlib import pyplot as plt


# importing data

df = pd.read_csv('NZ 2.csv')

df.head()
df.tail()
df.info()
print(df.shape)
print(df.nunique())
list(df)

# checking null 

Nu = df.isnull().values.any()

#outliers

sns.boxplot(df['service_city'])

# Histogram visualization

df.hist(figsize=(8, 8), bins=50, xlabelsize=8, ylabelsize=8);


#outliers

sns.boxplot(df["service_city"])

# Data Correlation

Data_corr = df.corr(method ='kendall') 

#Descriptive Statistics

Descriptive_Statistics = df.describe() 
print(Descriptive_Statistics)

# count value 

service_city = df["service_city"].value_counts() 
print(service_city)

y = list(df.service_city)
plt.hist(y) 
plt.show()

bookings = df["bookings"].value_counts() 

z = list(df.bookings)
plt.hist(z) 
plt.show()

# Grouping data

Grouping_Data = df.groupby(['service_city', 'payable']).mean() 












