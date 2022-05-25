import requests
from bs4 import BeautifulSoup
import csv

url = "http://www.alba.co.kr/"


def get_brand_job():
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')

    brand = soup.find(id="MainSuperBrand")
    links = brand.find_all('a', {"class": "goodsBox-info"})
    list = []
    for link in links:
        title = link.find("span", {"class": "title"}).text
        company = link.find("span", {"class": "company"}).text
        site = link['href']
        list.append({
            "title": title,
            "company": company,
            "site": site,
        })
    return list


brand_jobs = get_brand_job()


for jobs in brand_jobs:
    company_name = jobs['company']
    company_name = company_name.replace("/", "_")
    print(f"Writing for {company_name}..")

    open_csv = open(
        f"C:/Users/jey28/Desktop/js/pythonWebScraping/nomad/nomad_challenge/job/'{company_name}'.csv", 'w', encoding='utf-8-sig')

    writer = csv.writer(open_csv)
    html = requests.get(jobs['site'])
    soup = BeautifulSoup(html.text, 'html.parser')

    result = soup.find(id="NormalInfo")
    list_body = result.find("tbody").find_all("tr", {"class": ""})

    writer.writerow(['location', 'title', 'time', 'pay', 'reg_date'])

    for body in list_body:
        if body.find('td', {'class': 'local'}) is not None:
            location = body.find("td", {"class": "local"}).get_text()
            time = body.find("td", {"class": "data"}).get_text().strip()
            title = body.find("td", {"class": "title"}).find(
                "span", {"class": "title"}).get_text()
            pay = body.find("td", {"class": "pay"}).get_text()
            reg_date = body.find("td", {"class": "regDate"}).get_text()
            writer.writerow([location, title, time, pay, reg_date])
    open_csv.close()
