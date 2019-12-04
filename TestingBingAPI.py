# Bing API test script. Requires setting a Bing Search API V7 subscription key in your local environment variables
# TODO: We will probably need to write instructions for obtaining a key through MS Azure, and for setting the env variable

# Import required modules.
from azure.cognitiveservices.search.websearch import WebSearchAPI
from azure.cognitiveservices.search.websearch.models import SafeSearch
from msrest.authentication import CognitiveServicesCredentials

import os
import sys

# Add your Bing Search V7 subscription key to your environment variables.
if 'BING_SEARCH_V7_KEY' in os.environ:
    SUBSCRIPTION_KEY = os.environ['BING_SEARCH_V7_KEY']
else:
    print("Error: No Bing Search V7 API key set in environment variables")
    # TODO: will want to print out instructions for setting the env variable
    sys.exit()

# Instantiate the client and replace with your endpoint.
client = WebSearchAPI(CognitiveServicesCredentials(SUBSCRIPTION_KEY), base_url = "https://cs3300-bing-api-01.cognitiveservices.azure.com/bing/v7.0")

web_data = client.web.search(query="Python Jobs")
print("Searched")

'''
Web pages
If the search response contains web pages, the results' name and url
are printed.
'''
if hasattr(web_data.web_pages, 'value'):

    print("\r\nWebpage Results#{}".format(len(web_data.web_pages.value)))

    for i in range(len(web_data.web_pages.value)):
        web_page = web_data.web_pages.value[i]
        print("Page" + str(i))
        print("Web page name: {} ".format(web_page.name))
        print("Web page URL: {} ".format(web_page.url))

else:
    print("Didn't find any web pages...")
