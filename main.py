import requests as r
from bs4 import BeautifulSoup

url = 'https://7745.by/catalog/dreli'
response = r.get(url)
soup = BeautifulSoup(response.text, 'lxml')
# Парсить(что, в_формате)
card = soup.find('div', class_='catalog-item')  # какой элемент искать, метка для поиска
art = card.find('div', class_='articul')
title = card.find('a', class_='item-block_name')
price = card.find('div', class_='item-block_price-wrapper')
print(art.text)
print(title.text, 'https://7745.by' + title.get('href'))
print(price.text.strip().replace(' ', ''))
