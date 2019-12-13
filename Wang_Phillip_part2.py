#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Part 2
import csv

csvfile=open('dog_info.csv', 'w')
spamwriter = csv.writer(csvfile, delimiter=',')



holder=breed_page()
track=0

for item in holder: # Take info from each dog list and parse them into each respective category
    columns=[]
    index=[]
    count=1
 
    for items in item:
        
        count+=1 
        if count%2==0:
            items=items.replace(':','')
            columns.append(items)
        elif count%2==1:
            if 'Ranks' in items:
                tally=0
                total=0
                items=items.split(' ')
                try:
                    index.append(float(items[1]))
                except ValueError:
                    index.append(191)
            elif 'inches' in items:
                tally=0
                total=0
                items=items.replace('-',' ').split(' ')
                for number in items:
                    try:
                        float(number)
                        tally+=1
                        total+=float(number)
                    except TypeError:
                        pass
                    except ValueError:
                        pass
                if total==0:
                    index.append(total)
                else:
                    average=total/tally
                    index.append(average)
                    
            elif 'pounds' in items:
                items=items.replace('-',' ').split(' ')
                tally=0
                total=0
                for number in items:
                    try:
                        float(number)
                        tally+=1
                        total+=float(number)
                    except TypeError:
                        pass
                    except ValueError:
                        pass
                if total==0:
                    index.append(total)
                else:
                    average=total/tally
                    index.append(average)

            elif 'years' in items:
                items=items.replace('-',' ').split(' ')
                tally=0
                total=0
                for number in items:
                    try:
                        float(number)
                        items=(float(items[0])+float(items[1]))/2
                        index.append(items)
                    except TypeError:
                        pass
                    except ValueError:
                        pass
            else:
                try: #total==0: #index.append(items)
                    index.append(items)
                except ValueError:
                    #total>0:
                    tally+=1
                    average=total/tally
                    index.append(average)
                except TypeError:
                    pass
           
        if count==15:
            if track==0:
                spamwriter.writerow(columns)
                spamwriter.writerow(index)
                track+=1
            elif track>=1:
                spamwriter.writerow(index)
    
print('Done')     


#191

