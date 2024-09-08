# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 21:19:08 2022

@author: Harrison Du
"""
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.wait import WebDriverWait
import time 
from bs4 import BeautifulSoup
#import requests
import csv
import pandas as pd
from selenium.webdriver.support.ui import Select

#import numpy as np
f = open('C:/Users/Harrison Du/Desktop/scrape/columbia.csv', 'w',newline='', encoding="utf-8")
writer=csv.writer(f, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)


nameList = pd.read_csv('names.csv', encoding='utf-8')
nameArray = nameList.to_numpy(dtype='str',copy=False, na_value='NoDefault.no_default')
print(nameArray[0])

driver = webdriver.Chrome()

driver.get('https://cas.columbia.edu/cas/login?service=https://directory.columbia.edu/people/search')
time.sleep(2)
username = driver.find_element(By.XPATH,"//input[@name='username']")
password = driver.find_element(By.XPATH,"//input[@type='password']")
username.send_keys('pb2939')
password.send_keys('BeigeMamba824!')
privacy = driver.find_element(By.XPATH,"//button[@class='cu-privacy-notice-close']").click()
time.sleep(2)  
submit = driver.find_element(By.XPATH,"//input[@class='btn-submit']").click()
time.sleep(15)
driver.get(driver.current_url)
time.sleep(2)



n=0

dataCounter=0
print(nameArray.size)
i=0



while i<nameArray.size:
    nameToSearch= driver.find_element(By.XPATH,"//input[@name='filter.searchTerm']")
    nameToSearch.send_keys(nameArray[i])
    #time.sleep(10)
    time.sleep(0.1)
    search=driver.find_element(By.XPATH,"//input[@class='button2']").click()
    time.sleep(0.1)
    source = driver.page_source
    soup=BeautifulSoup(source,'lxml')
    
    
    
    #print(len(students))
    
    resultPage=soup.find("div",class_='page_number_result')
    pages=resultPage.find_all('li')
    pageCount=0
    for page in pages:
        try:
            url='https://directory.columbia.edu/people/search?page='+str(pageCount)
            driver.get(url)
            time.sleep(2)
            select=Select(driver.find_element(By.XPATH,"//select[@class='text']"))
            select.select_by_value('80')
            source = driver.page_source
            soup=BeautifulSoup(source,'lxml')
            time.sleep(2)
            pageCount+=1
            tableResults=soup.find("div",class_="table_results")
            students=tableResults.find_all("tr")
        except:
            pass
        
        for student in students:
            #print('test')
            td_values=student.find_all('td')
            row=''
            #Â
            #combine td2 and td3, td4 is email
            for td in td_values:
                row+= td.text+','
                print(td.text)
            writer.writerow(row)
            dataCounter+=1  
              
        
   
    print('\n', dataCounter,'\n')
    nameToSearch= driver.find_element(By.XPATH,"//input[@name='filter.searchTerm']")
    nameToSearch.clear()
    i+=1
n+=1
f.close()

time.sleep(2)
