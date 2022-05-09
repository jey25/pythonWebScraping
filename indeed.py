

import requests
from bs4 import BeautifulSoup

URL = f"https://kr.indeed.com/jobs?q=qa&limit=50&radius=25&vjk=2e794be49a16f1e7"

def extract_indeed_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class":"pagination"})

    links = pagination.find_all("a")

    pages = []

    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page


