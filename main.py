import requests as r
from bs4 import BeautifulSoup

url = 'https://7745.by/catalog/dreli'
response = r.get(url)
soup = BeautifulSoup(response.text, 'lxml')
# Парсить(что, в_формате)
card = soup.find('div', class_='styles_root__ti07r')  # какой элемент искать, метка для поиска
print(card)
