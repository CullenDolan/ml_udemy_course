# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Get the dataset
dataset = pd.read_csv('Position_Salaries.csv')

#Set the independent and dependent variables
x = dataset.iloc[:,1:2].values
y = dataset.iloc[:,2].values
"""
#Scale the Data
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
sc_y = StandardScaler()
x = sc_x.fit_transform(x)
y = sc_y.fit_transform(y)

#Split into train test sets
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)
"""
#Fit the data to the model with the regressor
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(x, y)

#Make the Prediction
y_pred = regressor.predict(6.5)

#Visualize the results
x_grid = np.arange(min(x), max(x), 0.01)
x_grid = x_grid.reshape((len(x_grid)), 1)
plt.scatter(x, y, color = 'red')
plt.plot(x_grid, regressor.predict(x_grid), color = 'blue')
plt.show()