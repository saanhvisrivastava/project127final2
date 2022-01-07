from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests
import pandas as pd

start_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
data=requests.get(start_url)
#print(data.text)

soup=BeautifulSoup(data.text,'html.parser')
star_table=soup.find('table')
#print(star_table)

temp_list=[]

table_rows=star_table.find_all('tr')
#print(table_rows)

for tr in table_rows: # For each tr finding all the td tags and store into td variable
    td=tr.find_all('td')
    row=[i.text.rstrip() for i in td]
    temp_list.append(row)
#print(temp_list)
#print(len(temp_list))

Star_name=[]
Distance=[]
Mass=[]
Radius=[]

for i in range(1,len(temp_list)):
    Star_name.append(temp_list[i][1])#row and column index
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])

#print(star_name)

df=pd.DataFrame(list(zip(Star_name,Distance,Mass,Radius)),columns=['Star_name','Distance','Mass','Radius'])
#combine related index value together
#print(df)

df.to_csv('bright_stars.csv')
#print(temp_list)
















