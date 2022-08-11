# from selenium.webdriver.common.keys import Keys
# import time
# from selenium import webdriver
# driver=webdriver.Chrome(r"C:\Users\Shayan\Desktop\New folder (3)\chromedriver")
# driver.get("https://divar.ir/s/tehran/buy-residential")
# time.sleep(3)
# previous_height=driver.execute_script('return document.body.scrollHeight')
# while True:
#     driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
#     time.sleep(1)
#     new_height=driver.execute_script('return document.body.scrollHeight')
#     if new_height == previous_height:
#         break
    

import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

import numpy as np , openpyxl
import pandas as pd


excel=openpyxl.Workbook()
sheet=excel.active
sheet.title="divar"
sheet.append(["ditails","price"])


driver=webdriver.Chrome(r"C:\Users\Shayan\Desktop\New folder (3)\chromedriver")
driver.get("https://divar.ir/s/tehran/buy-residential")
time.sleep(2)  # Allow 2 seconds for the web page to open
scroll_pause_time = 1 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
    
    
    
    
for i in range(100):
       
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    time.sleep(scroll_pause_time)
        
    soup = BeautifulSoup(driver.page_source, "html.parser")

    

    components=soup.find_all("div" , class_="kt-post-card__body")
   

    for component in components:
        
        name=component.h2.text
        price= component.find("div", class_="kt-post-card__description").text
        
        
        sheet.append([name , price ])
     
       

excel.save("divar.xlsx")    
            


