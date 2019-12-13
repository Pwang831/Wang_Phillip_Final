#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Part 3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




combine=pd.read_csv('dog_info.csv')
combine2=pd.read_csv('dog_adoption.csv')

df = pd.merge(combine, combine2, on='Breed')# Merge the two csv file into one

print(df[['Breed', 'Listings','Height']].corr()) # Run correlation analysis on selected pair
print(df[['Breed', 'Listings','AKC Breed Popularity']].corr())
print(df[['Breed', 'Listings','Weight']].corr())
print(df[['Breed', 'Listings','Life Expectancy']].corr())



