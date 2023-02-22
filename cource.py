import requests
from bs4 import BeautifulSoup
from config import link_page, headers

full_page = requests.get(link_page, headers)

soup = BeautifulSoup(full_page.content, 'html.parser')

convert = soup.findAll("div", {"class": "YMlKec fxKbKc"})[0].txt