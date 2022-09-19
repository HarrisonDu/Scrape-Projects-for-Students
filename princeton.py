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
f = open('C:/Users/Harrison Du/Desktop/scrape/princeton3.csv', 'w',newline='', encoding="utf-8")
writer=csv.writer(f, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
year=['2025']

alphabetList= pd.read_csv('alphabet.csv')
alphabet = alphabetList.to_numpy(dtype='str',copy=False, na_value='NoDefault.no_default')
#print(nameArray[1])

driver = webdriver.Chrome('C:/Users/Harrison Du/Desktop/scrape/chromedriver.exe')

driver.get('https://www.princeton.edu/search/people-advanced')
time.sleep(2)
#username = driver.find_element(By.XPATH,"//input[@name='loginX']")
#password = driver.find_element(By.XPATH,"//input[@name='password']")
#username.send_keys('')
#password.send_keys('')
#time.sleep(2)  
#submit = driver.find_element(By.XPATH,"//input[@type='submit']").click()
#time.sleep(2)
#print(driver.current_url)
driver.get(driver.current_url)
time.sleep(2)

n=0
dataCounter=0
o=0
while o<len(year):
    while n<len(alphabet):
        i=0
        extraKey=alphabet[n]
        yearNow=year[o]
        while i<len(alphabet):
            driver.get('https://www.princeton.edu/search/people-advanced')
            nameToSearch= alphabet[i]
            nameSearch = driver.find_element(By.XPATH,"//input[@name='f']").send_keys(nameToSearch)
            lastNameSearch = driver.find_element(By.XPATH,"//input[@name='l']").send_keys(extraKey)
            department = driver.find_element(By.XPATH,"//input[@name='d']").send_keys(yearNow)
            time.sleep(0.5)
            nameSearchGo = driver.find_element(By.XPATH,"//input[@name='d']").send_keys(Keys.RETURN)
            time.sleep(1)
            
            #driver.execute_script('var buttons = document.querySelectorAll("[data-testid=\'card-expand\']"); for(var i = 0; i < buttons.length;i++)\tbuttons[i].click();')
            #print(driver.current_url)
            driver.get(driver.current_url)
            
            time.sleep(1.7)
            source = driver.page_source
            soup=BeautifulSoup(source,'lxml')
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            try:
                studentTable=soup.find("div",class_="bordered")
                students = studentTable.find_all("div",class_='row')
                print('success')
                for student in students:
                    try:
                        name=student.find('h3').text
                        #print(name)
                        emailLink=student.find('div',class_='people-search-email columns small-12 medium-3')
                        email=emailLink.find('a').text
                        email1=email.replace('\t','')
                        category=student.find('div',class_='people-search-result-department columns small-12 medium-6 large-3').text
                        category1=category.replace('\n','')
                        category2=category1.replace('\t','')
                        print(name,email1,category2)
                        row=name+','+email1+','+category2
                        
                        writer.writerow(row)
                        dataCounter+=1
                    except:
                        pass
                try:
                    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                    time.sleep(0.5)
                    nextPage= driver.find_element(By.XPATH,"//a[@title='Go to next page']").click()
                    print('\n\n\n nextPage \n\n\n')
                    driver.get(driver.current_url)
                    time.sleep(1.5)
                    for student in students:
                        try:
                            name=student.find('h3').text
                            #print(name)
                            emailLink=student.find('div',class_='people-search-email columns small-12 medium-3')
                            email=emailLink.find('a').text
                            email1=email.replace('\t','')
                            category=student.find('div',class_='people-search-result-department columns small-12 medium-6 large-3').text
                            category1=category.replace('\n','')
                            category2=category1.replace('\t','')
                            print(name,email1,category2)
                            row=name+','+email1+','+category2
                            
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
        n+=1
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
