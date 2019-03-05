import pymongo
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

client = pymongo.MongoClient("148.251.102.221", 27017)
db = client.web_scrapping
collection = db.source

i = 1

for obj in collection.find({}, {'_id': False}):
    print("Base_url : ", obj['base_url'])
    driver.get(obj['base_url'])
    time.sleep(4)

    for j in range(len(obj) - 1):
        # print(obj['obj' + str(i)]['xpath'])
        # print(obj['obj' + str(i)]['type'])
        print(obj['obj' + str(i)]['field_name'])
        if obj['obj' + str(i)]['type'] == 'text':
            print(driver.find_element(By.XPATH, obj['obj' + str(i)]['xpath']).get_attribute('innerText'))
            time.sleep(4)

        elif obj['obj' + str(i)]['type'] == 'img':
            print(driver.find_element(By.XPATH, obj['obj' + str(i)]['xpath']).get_attribute('src'))
            time.sleep(4)

        elif obj['obj' + str(i)]['type'] == 'url':
            driver.find_element(By.XPATH, obj['obj' + str(i)]['xpath']).click()
            time.sleep(4)
            driver.switch_to.window(driver.window_handles[-1])  # this will select the active newest tab
            print(driver.title)

        elif obj['obj' + str(i)]['type'] == 'list':
            pass

        i += 1
        print("************************************************************************************")
driver.close()
