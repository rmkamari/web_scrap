from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

baseurl = "https://www.tabnak.ir/"

xpaths = {'title1': '//*[@id="home"]/div[3]/div[1]/div/div/section/div[2]/div[2]/div/div/div[2]/h3/a',
           'kol': '//*[@id="home"]/div[3]/div[1]/div/div/section',
           'submitButton':   "//input[@name='login']"
         }
driver = webdriver.Chrome()
driver.get(baseurl)
t1 = driver.find_element_by_xpath(xpaths['kol'])
print(t1.get_attribute('text'))
print(t1.get_attribute('href'))


driver.close()
# #Clear Username TextBox if already allowed "Remember Me"
# driver.find_element_by_xpath(xpaths['usernameTxtBox']).clear()
#
# #Write Username in Username TextBox
# driver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username)
#
# #Clear Password TextBox if already allowed "Remember Me"
# driver.find_element_by_xpath(xpaths['passwordTxtBox']).clear()
#
# #Write Password in password TextBox
# driver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)
#
# #Click Login button
# driver.find_element_by_xpath(xpaths['submitButton']).click()