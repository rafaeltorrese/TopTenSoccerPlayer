#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import pandas as pd


#base_url = 'https://mexicocity.craigslist.org/search/sss?query=carros&sort=rel'
base_url = 'https://listado.mercadolibre.com.mx/autos#D[A:autos]'

web_page = requests.get(base_url)


if web_page.status_code == requests.codes.ok:
    bs = BeautifulSoup(web_page.text, 'lxml')
    print('Connection was succesfull')

# All the first cars
list_of_cars = bs.find_all('div', class_='item__info ')
#
# The next section it was only for test
first_car = list_of_cars[0]
price = first_car.find('span' , class_='price__fraction').text
year, kilometer= first_car.find('div' , class_='item__attrs').text.strip().split('|')
kilometer = int(kilometer.replace('km' , ''))
description = first_car.find('span' , class_='main-title').text.strip()
location = first_car.find('div' , class_='item__location').text

# Here we get all data, only for the first page counter
data = {
        'Price':[float(car.find('span' , class_='price__fraction').text.replace(',' , '')) if car else 'none' for car in list_of_cars   ],
        'Year':[int(car.find('div' , class_='item__attrs').text.strip().split('|')[0]) if car else 'none' for car in list_of_cars ],
        'Km':[int(car.find('div' , class_='item__attrs').text.strip().split('|')[1].replace('km' , '')) if car else 'none' for car in list_of_cars ],
        'Description':[car.find('span' , class_='main-title').text.strip().split()[0] if car else 'none' for car in list_of_cars],
        'Location':[car.find('div' , class_='item__location').text if car else 'none' for car in list_of_cars]
        }

# Convert To Pandas DataFrame
CarsDF = pd.DataFrame(data)
CarsDF.index = CarsDF.index + 1
print(CarsDF)


# Save to csv
CarsDF.to_csv('Cars.csv' , index=False, sep=',' , encoding='utf-8')