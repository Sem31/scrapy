import requests

url = 'https://docs.python.org/3/'
response = requests.get(url)
html = response.content
print (html)