# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 23:29:44 2019

@author: lenovo
"""

from bs4 import BeautifulSoup
import requests
import lxml # Reading Web Page Text
import pandas as pd

base_url = "https://en.wikipedia.org/wiki/World_Soccer_(magazine)"



page = requests.get(base_url)

if page.status_code == requests.codes.ok:
    bs = BeautifulSoup(page.text, 'lxml')

# Fin something you specify in th hmtl
list_of_all_players = bs.find('table' ,class_='multicol').find('ul').find_all('li')
last_ten_players = list_of_all_players[-10:]

# Will hold our data

data ={
       'Year':[ name.find('span').previous_sibling.split()[0] if name else 'none' for name in last_ten_players ],
       'Country':[name.find('a')['title'] if name else 'none' for name in last_ten_players ],
       'Player':[name.find_all('a')[1].text if name else 'none' for name in last_ten_players ],
       'Team':[name.find_all('a')[2].text if name else 'none' for name in last_ten_players]
       }



first_player = last_ten_players[0]
year = first_player.find('span').previous_sibling.split()[0]
country = first_player.find('a')['title']
#for i,p in enumerate(first_player.find_all('a')):
#    print(i,p)

player = first_player.find_all('a')[1].text
team = first_player.find_all('a')[2].text


LastTenPlayersDataFrame = pd.DataFrame(data)
LastTenPlayersDataFrame.index = LastTenPlayersDataFrame.index + 1


LastTenPlayersDataFrame.to_csv('players_of_the_year.csv' , sep=',' , index=False , encoding='utf-8')