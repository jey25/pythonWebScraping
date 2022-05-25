import requests
from bs4 import BeautifulSoup

LIMIT = 10
url = f'https://kr.indeed.com/jobs?q=python&'


def get_last_page():

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


def extract_job(html):
    title = html.find("h2", {"class": "jobTitle"}
                      ).find("span", title=True).text
    company = html.find("span", {"class": "companyName"})
    company_anchor = company.find("a")
    if company_anchor is not None:
        company = company_anchor.string
    else:
        company = company.string
    location = html.find("div", {"class": "companyLocation"}).text
    find_id = html.find("h2", {"class": "jobTitle"})

    for id in find_id('a'):
        job_id = (id["data-jk"])
    return {'title': title, 'company': company, 'location': location, 'link': f"https://kr.indeed.com/viewjob?jk={job_id}"}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping page {page}")
        result = requests.get(f"{url}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "fs-unmask"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
