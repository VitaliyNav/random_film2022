import requests
from bs4 import BeautifulSoup as BS
import random

page = 1
ls = {}
while True:
    r = requests.get('https://w139.zona.plus/movies/filter/year-2022?page=' + str(page))
    html = BS(r.content, 'html.parser')
    items = html.select('ul.results > .results-item-wrap')
    if len(items) and page <= 3:
        print('--------------------------',page,'-----------------------------')
        for el in items:
            title = el.select('div.results-item-title')
            sulka = el.select('a.results-item')
            print(title[0].text)
            print('https://w139.zona.plus' + sulka[0].get('href'))
            ls[title[0].text] = 'https://w139.zona.plus' + sulka[0].get('href')

        page += 1

    else:
        break
print('--------------------------------------------------------------------------------------------------')
x = random.choice(list(ls))
print(x, ls.get(x))
print('--------------------------------------------------------------------------------------------------')
