#Web scraping is the process of extracting and collecting data from websites and storing it on a local machine or in a database.
#To start scraping websites you need requests, beautifoulSoup4 and a website.
# pip install requests and pip install beautifulsoup4


import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/datasets'

response = requests.get(url)
content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
print(soup.title)
print(soup.title.get_text()) #
print(soup.body)
print(response.status_code)
