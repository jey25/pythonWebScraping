

import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=qa&limit={LIMIT}&radius=25&vjk=2e794be49a16f1e7"

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


def extract_indeed_jobs(last_page):
    jobs = []
    # for page in range(last_page):
    result = requests.get(f"{URL}&start={0*LIMIT}")

    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("a", {"class" : "jcs-JobTitle"})

    for result in results:
        title = result.find("span", title=True).string
        company = result.find("span", {"class" : "companyName"}).string

        if(company is not None):
            company_anchor = company.find("a")
        if(company_anchor is not None):
            company = company_anchor.text
        else:
            company = company.text
        print(company)
        print(title)
  
    return jobs