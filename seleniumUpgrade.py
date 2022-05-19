
# selenium 4.0 이후 최신 버전 사용법 

# 아래 설치 또는 업그레이드

# pip install --upgrade pip
# pip install --upgrade selenium
# pip install webdriver_manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager


# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"]) 


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://www.naver.com/')