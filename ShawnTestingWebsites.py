
import sys  # for use in the sys.argv
import requests  # for use in getting the web page
import bs4  # for use of parsing the html file
import os
import re
import pprint
import openpyxl
from openpyxl.utils import get_column_letter

technology_regex = re.compile(r'''
    (tech|technology)
''', re.VERBOSE)

computer_regex = re.compile(r'''
    (computer|computer science)
''', re.VERBOSE)

careers_regex = re.compile(r'''
    (careers|career|jobs|job|professional|hiring|student)
''', re.VERBOSE)

email_regex = re.compile(r'''
    ([a-zA-Z0-9]+@[a-zA-Z0-9.]+)
''', re.VERBOSE)

string = 'https://www.google.com/search?q=microsoft+jobs'  # start of searching string

print('using: ' + string)  # print out to the user what exact search it is doing

res = requests.get(string)  # requests module pulls the html from the url

soup = bs4.BeautifulSoup(res.text, "html.parser")  # create a soup obj that parses the html from the request

p_elems = soup.select('div[class="kCrYT"] > a')

rank_dict = {}

for i in range(len(p_elems)):
    word = p_elems[i].get('href')
    index_value = word.find('&')
    url = p_elems[i].get('href')[7:int(index_value)]
    print('\nResult #' + str(i) + ': ' + url)

    new_res = requests.get(url)

    #print(new_res.text)

    html_soup = bs4.BeautifulSoup(new_res.text, 'html.parser')

    new_elems = html_soup.select('title')

    title = ''

    if new_elems:
        for j in range(len(new_elems)):
            print(new_elems[j].text)
            title = new_elems[j].text

    mo = technology_regex.findall(new_res.text.lower())

    tech_count = 0

    if mo:
        for j in mo:
            tech_count += 1

    mo = careers_regex.findall(new_res.text.lower())

    career_count = 0

    if mo:
        for j in mo:
            career_count += 1

    mo = email_regex.findall(new_res.text.lower())

    email_list = []

    if mo:
        for j in mo:
            email_list.append(j)

    computer_count = 0

    mo = computer_regex.findall(new_res.text.lower())

    if mo:
        for j in mo:
            computer_count += 1

    print('Tech Search hit count: ' + str(tech_count))
    print('Career Search hit count: ' + str(career_count))
    print('Computer Search hit Count: ' + str(computer_count))

    print('Email List:')

    for email in email_list:
        print('\t' + email)

    rank_dict[title] = {'Tech': tech_count, 'Career': career_count, 'Email List': email_list,
                        'Computer': computer_count, 'url': url}

pprint.pprint(rank_dict)

excel_file = openpyxl.Workbook()

sheet = excel_file.active

title_list = ['Title', 'Email', 'Career', 'Computer', 'Tech', 'URL']

iteration = 1

for value in title_list:
    cell = str(get_column_letter(iteration) + str(1))

    sheet[cell] = value

    iteration += 1

iteration = 2
for value in rank_dict:
    cell = str(get_column_letter(1) + str(iteration))
    sheet[cell] = value

    cell = str(get_column_letter(2) + str(iteration))

    message = ''

    for item in rank_dict[value]['Email List']:
        message += str(item + '\n')

    sheet[cell] = message

    cell = str(get_column_letter(3) + str(iteration))
    sheet[cell] = rank_dict[value]['Career']

    cell = str(get_column_letter(4) + str(iteration))
    sheet[cell] = rank_dict[value]['Computer']

    cell = str(get_column_letter(5) + str(iteration))
    sheet[cell] = rank_dict[value]['Tech']

    cell = str(get_column_letter(6) + str(iteration))
    sheet[cell] = rank_dict[value]['url']

    iteration += 1

excel_file.save('ShawnTestData.xlsx')

excel_file.close()
