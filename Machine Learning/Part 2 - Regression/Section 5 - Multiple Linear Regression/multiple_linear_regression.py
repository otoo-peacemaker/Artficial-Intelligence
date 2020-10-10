# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Encoding categorical data
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer([('encoder', OneHotEncoder(), [3])], remainder='passthrough')
#Encoding the Independent Variable state
X = np.array(ct.fit_transform(X), dtype=np.float)

# Avoiding the Dummy Variable Trap
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the y test on the X_Test set results
y_pred = regressor.predict(X_test)

# reshaping
y_pred.reshape(10,1)

# visualize the result
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')# maintain the same x-asxis and plot the predicted values
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


#Backward Elimination

import statsmodels.regression.linear_model as sm
"""
add a column of ones as integer dtype to independent values
"""
X = np.append(arr=np.ones((50,1)).astype(int), values = X, axis = 1)

#choosing a significant level usually 0.05, if p>0.05 for the highest values parameter, remove it

X_rem = X[:,[0,1,2,3,4,5]]
ols = sm.OLS(endog = y, exog = X_rem).fit()
ols.summary()

X1_rem = X[:,[0,1,3,5]]
ols = sm.OLS(endog = y, exog = X_rem).fit()
ols.summary()

X2_rem = X[:,[0,1,5]]
ols = sm.OLS(endog = y, exog = X_rem).fit()
ols.summary()
