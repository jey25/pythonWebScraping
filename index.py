import requests
from bs4 import BeautifulSoup

r = requests.get("https://stackoverflow.com/search?q=qa")

soup = BeautifulSoup(r.text, "html.parser")

print(soup)

