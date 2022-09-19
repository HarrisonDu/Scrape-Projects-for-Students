# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 21:19:08 2022

@author: Harrison Du
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time 
from bs4 import BeautifulSoup
import requests
import csv


url ='https://www.sinosplice.com/learn-chinese/chinese-vocabulary-lists/the-top-100-chinese-surnames'
r = requests.get(url)


soup=BeautifulSoup(r.text,'html.parser')

f = open('C:/Users/Harrison Du/Desktop/scrape/indianNames.csv', 'w',newline='', encoding="utf-8")
writer=csv.writer(f, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)


nameTable = soup.find('div',class_="row=wrapper-x")
names = nameTable.find_all('tr', class_="")

for name in names:
    nameRows=name.find_all('td')
    i=0
    for nameRow in nameRows:
        if i==2:
            writer.writerow(name.text)
            print(name.text)
        i+=1



#last_height = driver.execute_script("return document.body.scrollHeight;")


    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #new_height = driver.execute_script("return document.body.scrollHeight;")
    
    #if new_height == last_height:
     #   break
    #last_height = new_height

#csv_columns = ['Name','Email']

#csv_file = "People.csv"
#try:
 #   with open(csv_file, 'w') as csvfile:
  #      writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
   #     writer.writeheader()
    #    for data in my_dict:
           # writer.writerow(data)
#except IOError:
 #   print("I/O error")
#job_description
#content=soup.find_all('div',class_="c-card__social-links")

#for property in content:
 #   a = property.find('a')
  #  print(a)