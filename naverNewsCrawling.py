
import requests
from bs4 import BeautifulSoup
import pyautogui

keyword = pyautogui.prompt("검색어를 입력하세요. >>>")
lastPage = pyautogui.prompt("마지막 페이지 번호를 입력해 주세요.")
pageNum = 1
for i in range(1, int(lastPage) * 10, 10):
    print(f"{pageNum}페이지 입니다.----------------------------------")
    respones = requests.get(f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query={keyword}&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=92&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={i}', verify=False)
    html = respones.text
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select('.news_tit')

    for link in links:
        title = link.text
        url = link.attrs['href']
        print(title, url)
    pageNum = pageNum + 1