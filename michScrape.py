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
f = open('C:/Users/Harrison Du/Desktop/scrape/data.csv', 'w',newline='', encoding="utf-8")
writer=csv.writer(f, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)


nameList= pd.read_csv('names.csv')
nameArray = nameList.to_numpy(dtype='str',copy=False, na_value='NoDefault.no_default')
print(nameArray[1])

driver = webdriver.Chrome('C:/Users/Harrison Du/Desktop/scrape/chromedriver.exe')

driver.get('https://weblogin.umich.edu/?factors=UMICH.EDU&cosign-webdirectory.mc.itd&https://mcommunity.umich.edu/')
time.sleep(2)
username = driver.find_element(By.XPATH,"//input[@name='loginX']")
password = driver.find_element(By.XPATH,"//input[@name='password']")
username.send_keys('')
password.send_keys('')
time.sleep(2)  
submit = driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(2)
print(driver.current_url)
driver.get(driver.current_url)
time.sleep(2)

letters=[' a',' e',' i',' o',' u']
n=0
dataCounter=0
while n<len(letters):
    i=0
    extraKey=letters[n]
    while i<nameArray.size:
        nameToSearch= nameArray[i]
        nameSearch = driver.find_element(By.XPATH,"//input[@class='gwt-TextBox']").send_keys(nameToSearch)
        nameSearch = driver.find_element(By.XPATH,"//input[@class='gwt-TextBox']").send_keys(extraKey)
        time.sleep(0.1)
        nameSearchGo = driver.find_element(By.XPATH,"//button[@class='gwt-Button']").click()
        time.sleep(1)
        nameSearchGo = driver.find_element(By.LINK_TEXT, 'People').click()
        #driver.execute_script('var buttons = document.querySelectorAll("[data-testid=\'card-expand\']"); for(var i = 0; i < buttons.length;i++)\tbuttons[i].click();')
        #print(driver.current_url)
        driver.get(driver.current_url)
        time.sleep(0.5)
        source = driver.page_source
        soup=BeautifulSoup(source,'lxml')
        
        studentTable=soup.find("div",class_="tabularListPage")
        students = studentTable.find_all("tr")
        
        for student in students:
            try:
                if 'student' in (student.find('li').text).lower():
                    name=student.find('a').text
                    email=student.find('div',class_='uniqname').text+'@umich.edu'
                    category=student.find('li').text
                    print(name,email,category)
                    row=name+','+email+','+category
                    writer.writerow(row)
                    dataCounter+=1
            except:
                pass
        print('\n', dataCounter,'\n')
        i+=1
    n+=1
    

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