import sys, requests, bs4, os, re, pprint, multiprocessing, openpyxl
from multiprocessing import freeze_support, Manager
from openpyxl.utils import get_column_letter  # getting the get_colum_letter function
from googlesearch import search


res = requests.get('https://www.monster.com/jobs/search/?q=python&where=Colorado-Springs__2C-CO')

html_soup = bs4.BeautifulSoup(res.text, 'html.parser')

linkedin_page_elements = html_soup.select('h2[class="title"] > a')

company_linkedin_urls = []

if linkedin_page_elements:
    for i in linkedin_page_elements:
        company_linkedin_urls.append(i.get('href'))

for url in company_linkedin_urls:

    print('Using: ' + url)

    new_res = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})

    new_soup = bs4.BeautifulSoup(new_res.text, 'html.parser')

    company_page_elements = new_soup.select('footer[class="card-footer"] > a[id="AboutCompanyProfileLink"]')

    urls_two = []

    if company_page_elements:
        for i in company_page_elements:
            urls_two.append(i.get('href'))

    for item in urls_two:
        res_two = requests.get(item, headers={'User-agent': 'Mozilla/5.0'})

        print(res_two.text)

        break

        soup_two = bs4.BeautifulSoup(res_two.text, 'html.parser')

        monster_company_page_elements = soup_two.select('li[_ngcontent-fao-c5=""] > a')

        if monster_company_page_elements:
            for i in monster_company_page_elements:
                print('****** ' + i.get('href'))
    break