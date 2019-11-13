
import sys  # for use in the sys.argv
import requests  # for use in getting the web page
import bs4  # for use of parsing the html file
import os
import re
import pprint

technology_regex = re.compile(r'''
    (tech|technology)
''', re.VERBOSE)

careers_regex = re.compile(r'''
    (careers|career|jobs|job|professional|hiring|student)
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
    print('Result #' + str(i) + ': ' + url)

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

    print('Tech Search hit count: ' + str(tech_count))
    print('Career Search hit count: ' + str(career_count) + '\n')

    rank_dict[title] = {'Tech': tech_count, 'Career': career_count}

pprint.pprint(rank_dict)
