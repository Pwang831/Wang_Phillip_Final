#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Part 1
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import csv
import json
import matplotlib.pyplot as plt


csvfile=open('dog_adoption.csv', 'w') # Compile  and write a csv file for dog breeds and number of listings in CA
dog_adoption_header=['Breed', 'Listings'] # Create header for the dog_adoption csv file
adoption_writer = csv.writer(csvfile, delimiter=',')


adoption_writer.writerow(dog_adoption_header)# Write header


url = requests.get('https://www.akc.org/dog-breeds/?letter=A') # Get request from AKC website to obtain a list of official dog breeds
if url.status_code==200: # Checks url status, only proceed if status=200
    soup = BeautifulSoup(url.text, 'html.parser') # Use the variable soup to save the parsed info
    info=soup.find('select', attrs = {'class': 'custom-select__select'}) #Locate information of interest
    Breeds=info.get_text()
    Breeds_list=Breeds.split('\n')[2:-1]
    print('Status Code=Good')
else:
    print('Status Code Error', url.status_code)
def breed_page(): # Get background info for each dog breed

    holder=[]
    try:
        for i in Breeds_list[:]:  #Convert spaces in Breed Name to hyphens inorder for url to work
            if ' ' in i:
                i=i.replace(' ','-')
            else:
                pass
            holders=[]
            url2=requests.get('https://www.akc.org/dog-breeds/'+i.lower()) #Get request for AKC dog breeds
            soup2 = BeautifulSoup(url2.text, 'html.parser')
            info2= soup2.find_all('div', attrs = {'class': 'page-container'})[1]
            info3=info2.find_all('span')
            for data in info3:
                holders.append(data.get_text())
            temp=holders[:12]#Remove unnecessary information
            if '\n\n\n\n\n\nThe AKC has grouped all of the breeds that it registers into seven categories, or groups, roughly based on function and heritage. Breeds are grouped together because they share traits of form and function or a common heritage.\n\n\n' in temp:
                pos=temp.index('\n\n\n\n\n\nThe AKC has grouped all of the breeds that it registers into seven categories, or groups, roughly based on function and heritage. Breeds are grouped together because they share traits of form and function or a common heritage.\n\n\n')
                temp=holders[:pos] # Remove random text
                if 'The AKC has grouped all of the breeds that it registers into seven categories, or groups, roughly based on function and heritage. Breeds are grouped together because they share traits of form and function or a common heritage.' in temp:
                    temp=temp.remove['The AKC has grouped all of the breeds that it registers into seven categories, or groups, roughly based on function and heritage. Breeds are grouped together because they share traits of form and function or a common heritage.']
                    temp.append('Breed:') # Append new column called 'Breed'
                    temp.append(i) #'Appends the breed name'
                    holder.append(temp)#Appends filtered information of interest
                else:
                    temp.append('Breed:')# Same as above
                    temp.append(i)
                    holder.append(temp)
            elif 'Miscellaneous Class' in temp:
                    position=temp.index('Miscellaneous Class')
                    temp=holders[:pos+1]
                    holder.append(temp)#Appends filtered information of interest
               
            else:
                temp.append('Breed:')# Same as above
                temp.append(i)
                holder.append(temp)
        return holder
    except TypeError:
        pass   
    except ValueError:
        pass

breed_page()





def access_token(): #Get access token from petfinder api
    data = {
        'grant_type': 'client_credentials',
        'client_id': 'Gz7jkcjM4SX4pSFVUcYS0F9qnFR5Bk4QlvOXUiBhRHCPivhwnh', # API Key
        'client_secret': 'JX9Re1ulFddXFATcdn3xjVcy5OGLC8E293cy7e5e'} # API Secret

    response1 = requests.post('https://api.petfinder.com/v2/oauth2/token', data=data)
    obj=response1.json()
    # create a formatted string of the Python JSON object
    texts = json.dumps(obj, sort_keys=True, indent=4)
    rep_dict1=json.loads(texts)
    access_token=rep_dict1['access_token']
    
    return access_token
                                   
access_token=access_token()


def jprint(breed=None): # Get request using petfinder APi
    
    headers = {
        'Authorization': 'Bearer ' +access_token,}
    response2 = requests.get('http://api.petfinder.com/v2/animals?dog&breed='+breed+'&location=Ca', headers=headers)
    if response2.status_code==200:
        obj2=response2.json()
      
    
   

    # create a formatted string of the Python JSON object
        text = json.dumps(obj2, sort_keys=True, indent=4)
        rep_dict2=json.loads(text)
        total_count=('total_count:', rep_dict2['pagination']['total_count'])
        if ' ' in breed:# Converts spaces in breed name to hyphens inorder to match dog_info data set
                breed=breed.replace(' ','-')
        else:
            pass
        adoption_count=[breed,rep_dict2['pagination']['total_count']]#Grab number of adoption listing for each breed query
        return adoption_count
    else:
        print('KeyError', response2.status_code)
        
        return['Breed Not Found']
    
    


for i in Breeds_list[:]: #Driver function to get all Breed adoption listings and write them into dog_adoption csv
    adoption_count=jprint(i)
    adoption_writer.writerow(adoption_count)







print('Done')





# In[ ]:




