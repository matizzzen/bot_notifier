import requests
from random import randint as r
from bs4 import BeautifulSoup


def get_anek():
    page = r(1, 1141)
    req = requests.get(f'https://baneks.ru/{page}')
    html = BeautifulSoup(req.content, 'html.parser')
    items = str(html.p)
    items = items.replace('<br/>', '')
    items = items.replace('<p>', '')
    items = items.replace('</p>', '')
    print(items)
    return items
