import requests
from bs4 import BeautifulSoup

url = 'https://docs.python.org/3/'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html,'lxml')
table = soup.find('tbody', attrs={'class': 'stripe'})
print(soup.table.prettify())

list_of_row = []
for row in soup.table.findAll('tr'):
    list_of_cell=[]
    for cell in row.findAll('td'):
        print (cell.prettify())
        text = cell.text.replace('&nbsp;', '') # replace space from the text
        print (cell.text.replace('&nbsp;', ''))
        list_of_cell.append(text)
    print(list_of_cell)
    list_of_row.append(list_of_cell)
print("\n",list_of_row)