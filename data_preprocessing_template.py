# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 10:27:54 2017

@author: cudolan
"""

#start with importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("Data.csv")
#this means that we took all the rows
#and all the columns minus the last one
x = dataset.iloc[:,:-1].values 
y = dataset.iloc[:,3].values

#fill in missing data
#define the class
from sklearn.preprocessing import Imputer
#define the object
imputer = Imputer(missing_values = "NaN", strategy = 'mean', axis = 0) 
#fit imputer object to features
imputer = imputer.fit(x[:,1:3])#upper bound is excluded
x[:,1:3] = imputer.transform(x[:,1:3])

#categorize the data (encode text to numbers)
#define the class
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
#define the object
labelencoder_x = LabelEncoder()
#perform a method on the object
x[:,0] = labelencoder_x.fit_transform(x[:,0])
#need to prevent machine from thinking greater vals are better
#dummy encoding splits categories into seperate cols then only use 1 & 0
#define another object
onehotencoder = OneHotEncoder(categorical_features = [0])
#perform the method on the object
x = onehotencoder.fit_transform(x).toarray()
#now we need to categorize the dependent variable
#class created move to object with label encoder
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

#split data into test an training set
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

#feature scaling
#define the class
from sklearn.preprocessing import StandardScaler
#define the object 
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)
