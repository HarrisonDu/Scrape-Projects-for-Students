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


driver = webdriver.Chrome('C:/Users/Harrison Du/Desktop/scrape/chromedriver.exe')

driver.get('https://app.parkerdewey.com/auth/sign-in')
time.sleep(2)
username = driver.find_element(By.XPATH,"//input[@name='email']")
password = driver.find_element(By.XPATH,"//input[@name='password']")
username.send_keys('hd1202@nyu.edu')
password.send_keys('Du.Family2003')
time.sleep(2)  
submit = driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(2)
print(driver.current_url)
driver.get(driver.current_url)
time.sleep(10)
driver.execute_script('var buttons = document.querySelectorAll("[data-testid=\'card-expand\']"); for(var i = 0; i < buttons.length;i++)\tbuttons[i].click();')
time.sleep(60)

print(len(driver.window_handles))
source = driver.page_source



soup=BeautifulSoup(source,'lxml')
f = open('C:/Users/Harrison Du/Desktop/scrape/data.csv', 'w',newline='', encoding="utf-8")
writer=csv.writer(f, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

 
time.sleep(10)
jobs = soup.find_all("div",class_="c-panel c-card")


#last_height = driver.execute_script("return document.body.scrollHeight;")

for job in jobs:
    print('hi')
    jobName=job.find('h2',class_="c-card__title")
    #side_panel= job.find('div',class_="o-span-6 o-span-2-med o-span-1-lg")
    #start_date = side_panel.find('dd',class_="c-label-value__value")
    #print(start_date.text)
    jobDes = job.find('p')
    print(jobDes.text)
    try:
        jobImgSrcUnprocessed= job.find('img',src=True)
        jobImgSrc=jobImgSrcUnprocessed['src']
        print(jobImgSrc.text)
    except:
        pass
    writer.writerow(jobName.text)
   
    print(jobName.text)
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