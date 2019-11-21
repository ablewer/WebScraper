import requests
import bs4
from googlesearch import search

urls = []

for url in search('microsoft jobs', stop=50):
    urls.append(url)

print(len(urls))