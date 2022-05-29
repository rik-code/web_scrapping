import csv
import requests as r
from bs4 import BeautifulSoup

url = 'https://7745.by/catalog/lobziki'


def parse_catalog(url):
    par = {
        'limit': 10000
    }
    response = r.get(url, params=par)
    soup = BeautifulSoup(response.text, 'lxml')

    cards = soup.findAll('div', class_='catalog-item')  # находит все элементы по критерию и создает из них списов
    with open('lobziki.csv', 'w', encoding='utf-8', newline='') as file:
        headers = ['Артикул', 'Название', 'Ссылка', 'Цена']
        writer = csv.writer(file)  # эта штука пишет информацию в таблицу
        writer.writerow(headers)  # прошу закинуть в таблицу заголовки

        # перебираю карточки товара
        for card in cards:
            art = card.find('div', class_='articul')
            title = card.find('a', class_='item-block_name')
            price = card.find('div', class_='item-block_price-wrapper')
            price_digits = price.text.strip().replace(' ', '')
            row = [art.text,
                   title.text,
                   'https://7745.by' + title.get('href'),
                   price_digits
                   ]  # создаю строчку таблицы
            writer.writerow(row)  # записываю инфу в таблицу

parse_catalog(url)
