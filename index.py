from pydoc import source_synopsis
from tempfile import SpooledTemporaryFile
import requests
from bs4 import BeautifulSoup

URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=qa&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&salary&radius=25&l&fromage=any&limit=50&sort&psf=advsrch&from=advancedsearch&vjk=2e794be49a16f1e7"


indeed_result = requests.get(URL)
indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class":"pagination"})

pages = pagination.find_all("a")

spans = []

for page in pages:
    spans.append(page.find("span"))

print(spans[:-1])




