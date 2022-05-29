import csv
import requests as r
from bs4 import BeautifulSoup

url = 'https://7745.by/catalog/lobziki'


def parse_catalog(url):
    par = {
        'limit' : 10000
    }
    response = r.get(url, params=par)
    soup = BeautifulSoup(response.text, 'lxml')

    cards = soup.findAll('div', class_='catalog-item')  # какой элемент искать, метка для поиска
    with open('lobziki.csv', 'w', encoding='utf-8', newline='') as file:
        headers = ['Артикул', 'Название', 'Ссылка', 'Цена']
        writer = csv.writer(file)
        writer.writerow(headers)
        for card in cards:
            art = card.find('div', class_='articul')
            title = card.find('a', class_='item-block_name')
            price = card.find('div', class_='item-block_price-wrapper')
            row = [art.text,
                   title.text,
                   'https://7745.by' + title.get('href'),
                   price.text.strip().replace(' ', '')]
            writer.writerow(row)

parse_catalog(url)