**Meeting on 10/24/19:**
-	Added Python Project called webscraper to the github repository 
-	Also added main.py
-	Found out we need to install git so that pycharm can immediately pull and commit to the github automatically
-	Looking into apis for google, seems like a possible one was a json api
-	Found out that google limits searches in the api to 100 per day

**Research Questions:**
-	What data comes out of the Open Search API (the google search JSON API)?
-	Is it faster (or efficient) to use the API versus just pulling with the request module like we did in the homework?


**Testing from 11/13/2019**
-   Have to be careful with job hunting websites coming up
-   Linkedin does not like web-scraping it, possibly have to reconfigure parser to be more "user" like
-   As of now ShawnTestingWebsites.py searches for Microsoft jobs and gets data from the first 6 websites from google

**Testing from 11/20/2019**
-   Added basic excel output, basically takes the data from the already built dictionary but organizes it into an excel file
-   Will need more information and data to collect and organize but for now it's a very basic functioning prototype of the project

**Changelog from 11/21/2019**
-   turned the parsing into a function that could be passed to the multiprocessing
-   added basic functionality to multiprocessing with skeleton to allow for user determined input
-   added code to allow for googlesearch module which allows n number of searches. (locked out around 300-500)

**Testing from 11/21/2019**
-   Testing: URLs pull into a que which are currently being passed to the multiprocessing.  I found that there was excess
    printing after the call statement.  Will need to find what is causing this.  The dictionary can be controlled using
    the manager module.  - AMB

**Additions from 12/2/2019**
-   Added dictionary manager to multiprocessing to merge the dictionaries (possible might need tweaking)
-   Need to add the resume check and the email tester now.

**Testing from 12/2/2019**
-   Started testing the Bing Search API (through Microsoft Azure Cognitive Services) as a potential web search option.
