#!/usr/bin/env python

import pyperclip
import requests
from bs4 import BeautifulSoup

def get_H():
    page = requests.get('https://en.wikipedia.org/wiki/Horse')
    soup = BeautifulSoup(page.text, 'html.parser')
    text = soup.find('h1').get_text()
    return pyperclip.copy(text[0])

get_H()