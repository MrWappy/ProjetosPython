from bs4 import BeautifulSoup

import os

import requests

url = 'https://search.yahoo.com/search?p=temperatura+lisboa'
res = requests.get(url)
html_page = res.text

soup = BeautifulSoup(html_page, 'html.parser')

t = soup.find(attrs={'class': 'currTemp'})

c = (int(t.text)-32)/1.8

print(int(c), "ºC")


if c <= 10 and c > 0:
    print("utilizar um agasalho quente!")
elif c > 10 and c <= 20:
    print("Utilizar um agasalho leve!")
elif c > 20:
    print("Não precisa de agasalho!")
else:
    print("?")
os.system("pause")
