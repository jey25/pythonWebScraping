import requests
from bs4 import BeautifulSoup

jobs = {}


def get_jobs(term):
    res = []
    jobs_res = we_work_remote(term)
    res.extend(jobs_res)
    jobs_res = remoteok(term)
    res.extend(jobs_res)
    jobs_res = saram_in(term)
    res.extend(jobs_res)
    return res


def saram_in(term):
    global jobs
    key = 'saramin'
    if jobs.get(key):
        return jobs[key]
    url = f"https://www.saramin.co.kr/zf_user/search?search_area=main&search_done=y&search_optional_item=n&searchType=search&searchword={term}"

    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')

    job_list = soup.find("div", {"class": "content"})
    features = job_list.find_all("div", {"class": "item_recruit"})
    saramin_jobs = []
    for job in features:
        title = job.find("h2", {"class": "job_tit"}).get_text().replace(
            ',', '/').replace('\n', '')
        company = job.find("strong", {"class": "corp_name"}).get_text().replace(
            ',', '/').replace('\n', '')
        site = job.find("h2", {"class": "job_tit"}).find('a')['href']
        site = "https://www.saramin.co.kr" + site

        saramin_jobs.append({
            "title": title,
            "company": company,
            "site": site,
        })
    jobs[key] = saramin_jobs
    return saramin_jobs


def remoteok(term):
    global jobs
    key = 'remoteok'
    if jobs.get(key):
        return jobs[key]
    url = f"https://remoteok.com/remote-{term}-jobs"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }

    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'html.parser')

    job_list = soup.find(id="jobsboard")
    features = job_list.find_all('tr', {"class": "job"})
    remoteok_jobs = []
    for job in features:
        position = job.find("td", {"class": "company_and_position"})
        company = position.find("span", {"class": "companyLink"}).find(
            'h3').get_text().replace(',', '/').replace('\n', '')
        title = position.find("a", {"class": "preventLink"}).find(
            'h2').get_text().replace(',', '/').replace('\n', '')
        site = position.find("a")['href']
        site = "https://remoteok.com" + site

        remoteok_jobs.append({
            "title": title,
            "company": company,
            "site": site,
        })
    jobs[key] = remoteok_jobs
    return remoteok_jobs


def we_work_remote(term):
    global jobs
    key = 'wework'
    if jobs.get(key):
        return jobs[key]
    url = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={term}"
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')

    job_list = soup.find(id="job_list")
    features = job_list.find_all('li', {"class": "feature"})
    wework_jobs = []
    for feature in features:
        job = feature.find_all('a')[1]
        title = job.find("span", {"class": "title"}).get_text().replace(
            ',', '/').replace('\n', '')
        company = job.find("span", {"class": "company"}).get_text().replace(
            ',', '/').replace('\n', '')
        site = job['href']
        site = "https://weworkremotely.com" + site

        wework_jobs.append({
            "title": title,
            "company": company,
            "site": site,
        })
    jobs[key] = wework_jobs
    return wework_jobs
