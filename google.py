import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request

driver = webdriver.Chrome('C:\chromedriver\chromedriver')
driver.get('https://www.google.co.kr/imghp?hl=ko&ogbl')

elm = driver.find_element_by_css_selector('#sbtc > div > div.a4bIc > input')
elm.send_keys('장어')
elm.send_keys(Keys.ENTER)

SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector('.mye4qd').click()
        except:
            break
    last_height = new_height

images = driver.find_elements_by_css_selector('.rg_i.Q4LuWd')

count = 1

for image in images:
    image.click()
    time.sleep(3)
    img = driver.find_element_by_css_selector('.n3VNCb').get_attribute("src")
    urllib.request.urlretrieve(img, str(count) + ".jpg")
    count = count + 1

driver.close()
