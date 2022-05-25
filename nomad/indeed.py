import requests
from bs4 import BeautifulSoup

LIMIT = 10
url = f'https://kr.indeed.com/jobs?q=python&'


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
    jobs = []
    # for page in range(last_page):
    result = requests.get(f"{url}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "heading4"})
    for result in results:
        title = result.find("a", {"class": "jcs-JobTitle"}).find(
            "span", title=True).text
        company = result.find("span", {"class": "companyName"}).text
        print(company)

    return jobs
