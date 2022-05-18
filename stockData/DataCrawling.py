import requests
from bs4 import BeautifulSoup
import urllib3
import openpyxl

path = r'C:\Users\jey25\pythonWebScraping\stockData\data.xlsx'
wb = openpyxl.load_workbook(path)
ws = wb.active # 활성화 된 시트 선택


# InsecureRequestWarning 안뜨게 예외처리
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 종목 코드 리스트
codes = [
    '005930',
    '000660',
    '035720'
]
row = 2
for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url, verify=False)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    price = soup.select_one("#_nowVal").text
    price = price.replace(',', '')
    print(price)
    ws[f'B{row}'] = int(price)
    row += 1

wb.save(path)