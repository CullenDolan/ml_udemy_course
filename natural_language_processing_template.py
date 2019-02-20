import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('Restaurant_Reviews.tsv',  delimiter = '\t', quoting = 3)

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

#empty list
corpus = []
for i in range(0,1000):
    #only keep letters a-z lower and capital
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i]) 
    #remove capital letters
    review = review.lower()
    #seperate the words into different strings
    review = review.split()
    #get the stem word
    ps = PorterStemmer()
    #for loop to get rid of the excess words
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    #using the set function moves through the words faster
    #bring the words back into 1 string
    review = ' '.join(review)
    #add each review to the list
    corpus.append(review)

#create the bag of words model
from sklearn.feature_extraction.text import CountVectorizer 
cv = CountVectorizer(max_features = 1500)#max_features  parameters will ony get the most releveant reviews
x = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:,1].values

#split into test and training set
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 0)

##Feature scaling
#from sklearn.preprocessing import StandardScaler
#sc = StandardScaler()
#x_train = sc.fit_transform(x_train)
#x_test = sc.transform(x_test)

#Fit Naive Bayes to training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(x_train, y_train)

#predict the results
y_pred = classifier.predict(x_test)

#confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

