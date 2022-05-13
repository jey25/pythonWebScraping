import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request

driver = webdriver.Chrome('C:\chromedriver\chromedriver')
driver.get('https://www.google.co.kr/imghp?hl=ko&ogbl')

elm = driver.find_element_by_css_selector('#sbtc > div > div.a4bIc > input')
elm.send_keys('장어')
elm.send_keys(Keys.ENTER)

images = driver.find_elements_by_css_selector('.rg_i.Q4LuWd')

count = 1

for image in images:
    image.click()
    time.sleep(3)
    img = driver.find_element_by_css_selector('.n3VNCb').get_attribute("src")
    urllib.request.urlretrieve(img, str(count) + ".jpg")
    count = count + 1
