# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 23:29:44 2019

@author: lenovo
"""

from bs4 import BeautifulSoup
import requests
import lxml # Reading Web Page Text


base_url = "https://en.wikipedia.org/wiki/World_Soccer_(magazine)"



page = requests.get(base_url)

if page.status_code == requests.codes.ok:

    bs = BeautifulSoup(page.text, 'lxml')




