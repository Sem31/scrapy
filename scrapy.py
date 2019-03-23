import requests
from bs4 import BeautifulSoup

url = 'https://docs.python.org/3/'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
print (soup.prettify())