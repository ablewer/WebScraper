import requests
import bs4
from googlesearch import search

urls = []

for url in search('microsoft jobs', stop=20):
    urls.append(url)

print(urls)