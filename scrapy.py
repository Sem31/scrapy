import requests
from bs4 import BeautifulSoup

url = 'https://docs.python.org/3/'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html,'lxml')
table = soup.find('tbody', attrs={'class': 'stripe'})
print(soup.table)
