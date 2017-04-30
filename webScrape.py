from bs4 import BeautifulSoup

import requests

url2 = "http://extension.psu.edu/business/ag-safety/vehicles-and-machinery/general-safety-for-all-equipment/e31"

r2 = requests.get(url2)

data2 = r2.text

soup2 = BeautifulSoup(data2, "html5lib")

pennStateDiv = soup2.find_all('div', attrs={'id' : 'content-core'})

pennStateDiv = [str(item).replace('\u','') for item in pennStateDiv]
pennStateDiv = [str(item).replace('\n','') for item in pennStateDiv]