from bs4 import BeautifulSoup

import requests

url = "https://www.usda.gov/our-agency/about-usda/laws-and-regulations"

r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data, "html5lib")

usdaDivs = soup.find_all('div', attrs={'id' : 'block-usda-content'})