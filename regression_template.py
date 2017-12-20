#Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Get the data set
dataset = pd.read_csv('INSERT_FILE_NAME.csv')

#Define the dependent (Y) and independent Variables (X)
x = dataset.iloc[:,1:2].values
y = dataset.iloc[:,2].values

#Split Data Set
"""from sklearn.cross_validation import train_test_split
x_train, y_train, x_test, y_test = train_test_split(x,y, train_size = 0.2, random_state = 0)"""

#fit regression model to dataset

#Predict previos salary with polynomila gression
y_pred = regressor.predict(6.5)

#Visualize linear regression
x_grid = np.arange(min(x),max(x),step = 0.01)
x_grid = x_grid.reshape(len(x_grid), 1)
plt.scatter(x,y, color = 'red')
plt.plot(x_grid, regressor.predict(x_grid), color = 'blue')
plt.title("Regression Model")
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()
