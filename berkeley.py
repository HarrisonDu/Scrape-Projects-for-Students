# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 19:54:30 2022

@author: Harrison Du
"""
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
f = open('C:/Users/Harrison Du/Desktop/scrape/berkeley.csv', 'w',newline='', encoding="utf-8")
writer=csv.writer(f, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#year=['2023','2024','2025']

nameList= pd.read_csv('names.csv')
nameArray = nameList.to_numpy(dtype='str',copy=False, na_value='NoDefault.no_default')
#print(nameArray[1])
extra=[' a',' e',' i',' o',' u']
driver = webdriver.Chrome('C:/Users/Harrison Du/Desktop/scrape/chromedriver.exe')

driver.get('https://stanfordwho.stanford.edu/people')
time.sleep(4)
#username = driver.find_element(By.XPATH,"//input[@name='loginX']")
#password = driver.find_element(By.XPATH,"//input[@name='password']")
#username.send_keys('huangcat')
#password.send_keys('Markers10!07')
#time.sleep(2)  
#submit = driver.find_element(By.XPATH,"//input[@type='submit']").click()
#time.sleep(2)
#print(driver.current_url)
time.sleep(2)

#n=0
dataCounter=0
o=0
while o<len(nameArray):
        i=0
        while i<len(extra):
            try:
                extraKey=extra[i]
                driver.get('https://stanfordwho.stanford.edu/people')
                nameToSearch= nameArray[i]
                nameSearch = driver.find_element(By.XPATH,"//input[@class='input-search']").send_keys(nameToSearch)
                lastNameSearch = driver.find_element(By.XPATH,"//input[@class='input-search']").send_keys(extraKey)
                
                time.sleep(1)
                x=0
                    
                nameSearchGo = driver.find_element(By.XPATH,"//input[@class='input-search']").send_keys(Keys.RETURN)
                department = driver.find_element(By.XPATH,"//input[@id='Filter192']").send_keys('Undergraduate')
                time.sleep(1)
                driver.get(driver.current_url)
                time.sleep(1)
                for x in range(200):
                    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                    time.sleep(0.1)
                
                
                #driver.execute_script('var buttons = document.querySelectorAll("[data-testid=\'card-expand\']"); for(var i = 0; i < buttons.length;i++)\tbuttons[i].click();')
                #print(driver.current_url)
                source = driver.page_source
                soup=BeautifulSoup(source,'lxml')
                #driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                try:
                    studentTable=soup.find("div",class_="people-directory")
                    students = studentTable.find_all("li",class_='people__list__item')
                    print('success')
                    for student in students:
                        try:
                            name=student.find('a',class_='person__data__name').text
                            #print(name)
                            emailLink=student.find('span',class_='sidebar-detail')
                            email=emailLink.find('a').text
                            category=student.find('div',class_='person__data__department').text
                            print(name,email,category)
                            row=name+','+email+','+category
                            
                            writer.writerow(row)
                            dataCounter+=1
                        except:
                            pass
                  
                
                except:
                    pass
            except:
                pass
                
            
            print('\n', dataCounter,'\n')
            i+=1
        #n+=1
        o+=1
    

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
