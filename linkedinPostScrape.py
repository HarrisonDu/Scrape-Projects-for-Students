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
f = open('C:/Users/Harrison Du/Desktop/scrape/linkedin.csv', 'w',newline='', encoding="utf-8")
writer=csv.writer(f, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)


#nameList= pd.read_csv('names2.csv')
#nameArray = nameList.to_numpy(dtype='str',copy=False, na_value='NoDefault.no_default')
#print(nameArray[1])

driver = webdriver.Chrome('C:/Users/Harrison Du/Desktop/scrape/chromedriver.exe')

driver.get('https://www.linkedin.com/feed/update/urn:li:activity:6952985111382429696/')
time.sleep(1)
signIn = driver.find_element(By.XPATH,"//a[@class='no-content-card__button no-content-card__button--primary']").click()
time.sleep(2)
driver.get(driver.current_url)
time.sleep(2)
username = driver.find_element(By.XPATH,"//input[@name='session_key']")
password = driver.find_element(By.XPATH,"//input[@type='password']")
username.send_keys('')
password.send_keys('')
time.sleep(0.5)  
submit = driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(15)
driver.get(driver.current_url)
time.sleep(10)
source=driver.page_source
time.sleep(2)
soup=BeautifulSoup(source,'lxml')

#letters=[' a', 'e',' i',' o',' u']
#n=0

dataCounter=0
#print(len(letters))
#print(nameArray.size)
m=0
def loadMore():
   try:
      global m
      load=driver.find_element(By.XPATH,"//button[@class='comments-comments-list__load-more-comments-button artdeco-button artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view']").click()
      m+=1
      print(m)
   except:
        pass
        
for i in range(240):
    loadMore()
time.sleep(20)   
#time.sleep(300)
#commentSection= soup.find('div',class_='comments-comments-list comments-comments-list--expanded')
#users = soup.find_all('article',class_='comments-comment-item comments-comments-list__comment-item')

users = soup.find_all('article',class_='comments-comment-item comments-comments-list__comment-item')

#while True:
 #   try:
  #      loadMore=driver.find_element(By.XPATH,"//button[@class='comments-comments-list__load-more-comments-button artdeco-button artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view']").click()
   # except:
    #    break


for user in users:
    print('success')
    try:
        time.sleep(0.8)
        name=user.find('span',class_="comments-post-meta__name-text hoverable-link-text").get_text()
        print('successOne')
        emailOuter=user.find('div',class_='feed-shared-text relative')#class_='comments-comment-item__main-content feed-shared-main-content--comment t-14 t-black t-normal').get_text()
        email=emailOuter.find('a').text
        print('successTwo')
        category=user.find('span',class_="comments-post-meta__headline t-12 t-normal t-black--light").get_text()
        print(name,email,category)
        row=name+','+email+','+category
        writer.writerow(row)
        dataCounter+=1
    except:
        pass
print('\n', dataCounter,'\n')

    

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