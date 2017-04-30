from bs4 import BeautifulSoup

import requests

url = raw_input("Enter a website to extract the URL's from: ")

r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data, "html5lib")

usdaDivs = soup.find_all('div', attrs={'id' : 'block-usda-content'})

for div in usdaDivs:
    print div.find_all('p')