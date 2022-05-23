import requests
from bs4 import BeautifulSoup

LIMIT = 10
url = f'https://kr.indeed.com/jobs?q=python&start={LIMIT}&vjk=6dd48f3771d01215'


def extract_indeed_pages():
    site = requests.get(url)

    html = site.text
    soup = BeautifulSoup(html, "html.parser")

    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all('a')

    pages = []
    for link in links[1:-1]:
        pages.append(int(link.text))

    max_pages = pages[-1]
    return max_pages


def extract_indeed_jobs(last_page):
    for page in range(last_page):
        print(page*LIMIT)
