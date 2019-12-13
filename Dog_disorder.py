#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

Dog_list=[]
Disorder_column=[]
disorder=[]
url = requests.get('https://cidd.discoveryspace.ca/breeds/overview.html') # Get request for cidd to get disorder for each dog breed
csvfile=open('disorder_info.csv', 'w')
dis_writer = csv.writer(csvfile, delimiter=',')



soup = BeautifulSoup(url.text, 'html.parser')
info=soup.find('div', attrs = {'class': 'item-list'})
for data in info.find_all('a'): # Finds all breed names and compiles them into a list
    Dog_list.append(data.get_text())

def breed_disorder(): # Finds all documented disorder associated to a respective dog breed 
    
    disorder_column=[]
    breed={}
    try:
        for dog in Dog_list[:]:
            disorder_string=''
            disorder_holder=[]
            disorder_temp=[]
            print(dog)
            if ' ' in dog:# Fixes spaces in names
                dog=dog.replace(' ','-')
            else:
                pass
           
            url2=requests.get('https://cidd.discoveryspace.ca/breed/' + dog.lower() + '.html')
           
            soup2 = BeautifulSoup(url2.text, 'html.parser')
            info2= soup2.find('div', attrs = {'class': 'content clear-block'})
            
            for data in info2.find_all('div', attrs = {'class': 'disorder-label'}):
                
                labels=data.get_text()
                disorder_column.append(labels)
                
    
                next_data=data.find_next_sibling().get_text().split('-')
                print(next_data)
                if len(next_data)==1:
                    
                    disorder_temp.append(next_data)
                    
                else:
                    pass
   
            for item in disorder_temp:
                for inner in item:
                    disorder_holder.append(inner)
       
            pair=zip(disorder_column,disorder_holder)
            pair=list(pair)
            breed[dog]=pair
        return breed
        
    except TypeError:
        pass
    except ValueError:
        pass
        
breed=breed_disorder()


def unpack(): # Take info for each dog list and parse them into respective categories
    columns=[]
    count=0
    for i in Dog_list[:2]:# Make sure the list indices matches above
        count+=1
        disorder=[]
        if ' ' in i:# Fixes spaces in names
            i=i.replace(' ','-')
        else:
            pass
        packed_items=breed[i]
        #for unpack in packed_items:
           # print(unpack[1])
        
        for item in packed_items:
            
            disorder.append(item[1])
        print(disorder)
        disorder.append(count)
        dis_writer.writerow(columns)
        
        #cur.execute('INSERT INTO Disorder VALUES (?,?,?,?,?)', disorder)
        
unpack()    
print('Done')


# In[ ]:


import requests
from bs4 import BeautifulSoup

Disorder_list=[]
url2 = requests.get('https://cidd.discoveryspace.ca/disorder/overview.html')# Get request for cidd to get disorder for each dog breed
soup = BeautifulSoup(url2.text, 'html.parser')
info=soup.find_all('div', attrs = {'class': 'item-list'})

for data in info:
    #print(data.get_text())# Finds all breed names and compiles them into a list
    data2=data.find_all('a')
    for i in data2:
        Disorder_list.append(i.get_text())
print(Disorder_list)

