from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from pymongo import MongoClient


driver = webdriver.Chrome()
driver.get("https://www.farsnews.com/")
time.sleep(4)
a = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[1]/div/div[1]/div[2]/section[1]/div/ul')
print(a.text)
# print(a.get_attribute("innerHTML"))
# print(a.location)
driver.find_element(By.XPATH, '/html/body/div[2]/main/div[1]/div/div[1]/div[2]/section[2]/ul/li[3]/a').click()
time.sleep(4)
print(driver.find_element(By.XPATH, '//*[@id="chosen-news"]/div[3]/div/ul').get_attribute('innerText'))
time.sleep(3)
print("img: ")
print(driver.find_element(By.XPATH, '/html/body/div[2]/main/div[1]/div/div[1]/div[1]/section[1]/div/a/img').get_attribute('alt'))
print(driver.find_element(By.XPATH, '/html/body/div[2]/main/div[1]/div/div[1]/div[1]/section[1]/div/a/img').get_attribute('src'))
print('news page: ')
driver.find_element(By.XPATH, '/html/body/div[2]/main/div[1]/div/div[1]/div[1]/section[2]/ul/li[1]/div[2]/a/div').click()
driver.switch_to.window(driver.window_handles[-1])  # this will select the active newest tab
print(driver.title)
time.sleep(5)
print(driver.find_element(By.XPATH, '/html/body/div[2]/main/div[1]/div/div[1]/div[1]/div[1]').get_attribute('innerText'))

driver.close()

"""
----------
LOGIN
    user  ==> xpath
    pass  ==> xpath
----------                                          ====== Origin Page (First Page)
SCRAP  =============================================
Each ITEM:                                           ====== News Page
    3 part:
        1 field name
        2 xpath
        3 type
            1 text
            2 img
            3 url  ==> click
            4 list ==> <ul><li>
"""
