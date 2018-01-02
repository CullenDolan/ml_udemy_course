"""
review btc white paper with NLP
"""
#import libabries
import requests 
from bs4 import BeautifulSoup
import nltk
import matplotlib.pyplot as plt
import re

#get and clean content from the page
page = requests.get('http://nakamotoinstitute.org/bitcoin/')
type(page) #prints type of content
html = page.text #saves text
soup = BeautifulSoup(html, 'html.parser')
type(soup)
soup.title # extract title (soup.title.string extracts as a string)
soup.findAll('h2')[:4] #find specific number of a certain tag
text = soup.get_text()

#make each word a token
tokens = re.findall('\w+', text)
tokens[:10]

#lower case for all words
words = []

for word in tokens:
    words.append(word.lower())
words[:8]

#identify stop letters 'the', 'and', 'or'
stop_words = nltk.corpus.stopwords.words('english')
stop_words[:10]

#remove all stop_words from list
words_ns = []

for word in words:
    if word not in stop_words:
        words_ns.append(word)

page.status_code #anything satrting w/ a 2 is good

page.content #loads HTML content from site

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify()) #formats everything in a semi readable format

list(soup.children)
[type(item) for item in list(soup.children)]

#gets all text
#h2 = heades, p = body text/equations, ol = bullets

headers = soup.find_all('h2')
bullets = soup.find_all('ol')
text = soup.find_all('p')

list(text.children)
white_paper = pd.DataFrame(text)
header_frame = pd.DataFrame(headers)
text.dispersion_plot('bitcoin')
sorted(set([white_paper]))
