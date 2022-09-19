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
import pandas as pd
import numpy as np
#import html.parser as HTMLParser
import html as html


f = open('C:/Users/Harrison Du/Desktop/scrape/linkedin.csv', 'w',newline='', encoding="utf-8")
writer=csv.writer(f, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

e= open('linkedinScrapeXML.xml','r',encoding='utf-8')

source=e.read()
#print(source)
soup = BeautifulSoup(html.unescape(source), 'html.parser')

users = soup.find_all('div',class_='comments-post-meta__profile-info-wrapper display-flex')
dataCounter=0

for user in users:
    print('success')
    try:
        name=user.find('span',)
        print('successOne')
        print(name)
        emailOuter=user.find('div',class_='feed-shared-text relative')#class_='comments-comment-item__main-content feed-shared-main-content--comment t-14 t-black t-normal').get_text()
        email=emailOuter.find('a')
        print('successTwo')
        category=user.find('span',class_="comments-post-meta__headline t-12 t-normal t-black--light")
        print(name,email,category)
        row=name+','+email+','+category
        writer.writerow(row)
        dataCounter+=1
    except:
        pass
print('\n', dataCounter,'\n')
print(len(users))

    

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