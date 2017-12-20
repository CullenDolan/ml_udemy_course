#Classifer
#Import the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Get the data
dataset = pd.read_csv('INSERT_FILE_NAME.csv')

#Define the independent and dependent variables
#iloc is an integer based position identifier for indexing
x = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:,4].values


#Split the Data into testing and Training set
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)

#Feature Scaling using Standard Sclaer
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler() 
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)

#Fit model to training set
#create the classifier here

#Predict test set results with the __ model
y_pred = classifier.predict(x_test)

#Evaluate ____ model with Confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)

#Visualize the results
from matplotlib.colors import ListedColormap
x_set, y_set = x_test, y_test
x1, x2 = np.meshgrid(np.arange(start = x_set[:, 0].min() - 1, stop = x_set[:, 0].max() + 1, step = 0.01),np.arange(start = x_set[:, 1].min() - 1, stop = x_set[:, 1].max() + 1, step = 0.01))
plt.contourf(x1, x2, classifier.predict(np.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape), alpha = 0.75, cmap = ListedColormap(("red","green")))
plt.xlim(x1.min(),x1.max())
plt.ylim(x2.min(), x2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1], c = ListedColormap(("red", "green"))(i), label = j)
plt.show()

#Visualize the results
from matplotlib.colors import ListedColormap
x_set, y_set = x_train, y_train
x1, x2 = np.meshgrid(np.arange(start = x_set[:, 0].min() - 1, stop = x_set[:, 0].max() + 1, step = 0.1),np.arange(start = x_set[:, 1].min() - 1, stop = x_set[:, 1].max() + 1, step = 0.1))
plt.contourf(x1, x2, classifier.predict(np.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape), alpha = 0.75, cmap = ListedColormap(("red","green")))
plt.xlim(x1.min(),x1.max())
plt.ylim(x2.min(), x2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1], c = ListedColormap(("red", "green"))(i), label = j)
plt.show()
