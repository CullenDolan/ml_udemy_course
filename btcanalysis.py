# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 09:53:18 2018

@author: cudolan
"""

import requests 
from bs4 import BeautifulSoup
import pandas as pd
import nltk
nltk.download()
#call the webpage
page = requests.get('http://nakamotoinstitute.org/bitcoin/')
#confirm the connection was successful
page.status_code #anything satrting w/ a 2 is good
#print all the html content
page.content #loads HTML content from site

soup = BeautifulSoup(page.content, 'html.parser')
#formats everything in a semi readable format
print(soup.prettify())

list(soup.children)
[type(item) for item in list(soup.children)]

#gets all text
#h2 = heades, p = body text/equations, ol = bullets

headers = soup.find_all('h2')
bullets = soup.find_all('ol')
text = soup.find_all('p')


white_paper = pd.DataFrame(text)
header_frame = pd.DataFrame(headers)
