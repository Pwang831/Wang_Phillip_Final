#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




combine=pd.read_csv('dog_info.csv')
combine2=pd.read_csv('dog_adoption.csv')

df = pd.merge(combine, combine2, on='Breed')# Merge the two csv file into one

df[['Breed', 'Listings','Height']].corr() # Run correlation analysis on selected pair
df[['Breed', 'Listings','AKC Breed Popularity']].corr()
df[['Breed', 'Listings','Weight']].corr()


