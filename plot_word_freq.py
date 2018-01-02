"""
review btc white paper with NLP
"""
#import libabries
import requests 
from bs4 import BeautifulSoup
import nltk
import matplotlib.pyplot as plt
import re
from nltk.tokenize import RegexpTokenizer


#function to get, clean, and plot word frequency from HTML text
def plot_word_freq(url, Samples):
    page = requests.get(url)
    html = page.text 
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    tokenizer = RegexpTokenizer('\w+')
    tokens = tokenizer.tokenize(text)
    
    words = []
    for word in tokens:
        words.append(word.lower())
        
    stop_words = nltk.corpus.stopwords.words('english')
    
    words_ns = []
    for word in words:
        if word not in stop_words: 
            words_ns.append(word)
    
    freqdist1 = nltk.FreqDist(words_ns)
    freqdist1.plot(Samples)
