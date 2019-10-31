# I understand the want to use of JSON files and the API now. Just using the the web-scrapping module will result in a
# a lot of pain for ourselves.

import requests
import bs4


# A test of the github features

url = 'https:www.google.com/search?q=tree+farms+colorado'

res = requests.get(url)

p_elems = bs4.BeautifulSoup(res.text, 'html.parser')

