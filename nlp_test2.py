# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 13:49:42 2018

@author: cudolan
"""

import nltk
nltk.download()
from nltk.book import *

#concordance allows you to search for specific words in context
text1.concordance('monstrous')

x = 'money'
text5.similar(str(x))
text7.similar(str(x))
text8.similar(str(x))

text2.common_contexts(['very', 'monstrous'])

text7.dispersion_plot(['finance', 'money', 'bitcoin'])
text3.generate()
len(text7)

t1 = len(text1)
t2 = len(text2)
t3 = len(text3)


print (t1)
print (t2)
print (t3)


sorted([t1, t2, t3])

sorted(set(text8))

len(text8) / len(set(text8))
text8.count('single')