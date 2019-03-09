from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time


# baseurl = "https://www.farsnews.com"
# baseurl = "https://www.tabnak.ir"
baseurl = 'https://www.mashreghnews.ir'


xpaths = {'title1': '//*[@id="home"]/div[3]/div[1]/div/div/section/div[2]/div[2]/div/div/div[2]/h3/a',
           'kol': '//*[@id="home"]/div[3]/div[1]/div/div/section',
           'submitButton':   "//input[@name='login']"
         }

# pageContent = requests.get(baseurl)
# tree = html.fromstring(pageContent.content)
# print(tree)
# data = tree.xpath('//*[@id="home"]/div[3]/div[1]/div/div/aside[3]/section/div[3]/div[2]/section/div')
# for i in data:
#     print(i)
# raw_html = tree.cssselect("div.div_class ul > li")
# raw_html = tree.xpath('//*[@id="home"]/div[3]/div[1]/div/div/aside[3]/section/div[3]/div[2]/section/div')
# for item in raw_html:
#     print(item.text_content())
driver = webdriver.Chrome()
driver.get(baseurl)
data = driver.find_element_by_xpath('//*[@id="box16"]/div')
list_html = data.get_property("innerHTML")
soup = BeautifulSoup(list_html, 'html.parser')

links = soup.find_all("a")

for l in links:
    if baseurl in l:
        print(l['href'])
    else:
        driver.get(baseurl + l['href'])
        time.sleep(4)
        print(baseurl + l['href'])
driver.close()
