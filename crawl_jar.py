import os
import requests
from pathlib import Path
import json
import sqlite3
import time
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
from datetime import datetime, timedelta
''' За сайта jarcomputers.com е компютърна фирма на Българския пазар, предлагаща техника като лаптопи, настолни компютри, 
компютърни компоненти, периферия и други.
Задача
Да се извлече информация за предлаганите лаптопи (https://www.jarcomputers.com/Laptopi_cat_2.html?ref=c_1) марка Lenovo.
Данните, които трябва да се съхранят в база данни (MrelativedeltaySQL или MongoDB) са:
    • модел 
    • цена 
    • размер на екран 
Да се състави потребителски интерфейс в който да се представят таблично получените данни.
Трябва да има поле за филтриране по размер на екран и възможност за сортиране (в намаляващ/увеличаващ ред) по цена.
Забележка
Вашият crawler трябва да се съобразява с правилата в https://www.jarcomputers.com/robots.txt.'''

links=[]

# URL of the website to crawl
response = requests.get('https://www.jarcomputers.com/Laptopi_cat_2.html?ref=c_1')
if response.status_code == 200:
    response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all( href = re.compile('lenovo'))

url = ""


response = requests.get('https://www.jarcomputers.com/Laptopi_cat_2.html?ref=c_1')
if response.status_code == 200:
    response.content
else:
    print(f"Failed to fetch {url}, status code: {response.status_code}")
    
soup = BeautifulSoup(response.text, 'html.parser')


# Extract information based on the HTML structure of the page


#  Print all laptop names
laptop_names = soup.find_all( href = re.compile('lenovo'))
for laptop_name in laptop_names:
    print(laptop_name.text.strip())

# Print all laptop prices
laptop_prices = soup.select('.price')
for laptop_price in laptop_prices:
    #print(laptop_price.text.strip())

    print(f"Laptop: {laptop_name.text}, Price: {laptop_price.text}")

#for link in links:
    #if link not in links:
        #links.append(link)
    #print(link) 