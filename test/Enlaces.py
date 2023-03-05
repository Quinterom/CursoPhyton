from bs4 import BeautifulSoup
import requests
import numpy as np

enlaces = []
html=requests.get('https://es.wikipedia.org/wiki/Emilio_Mola').text

soup=BeautifulSoup(html, "html.parser")

for link in soup.findAll('a'):
    data = link.get("href")
    if data is not None:
        if "https:" in data:
            enlaces.append(data)
np.savetxt('datos.csv', enlaces, delimiter=',', fmt="%s")
