# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 21:24:37 2020

@author: Kwesi-Welbred

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
importing the dataSet and selecting the dependant and 
independance data from the dataSet

"""
dataset = pd.read_csv("Data.csv")
dataset
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:,3].values


"""
PERFORMING PREPROCESSING 

filling the missing values using the sci-kit learn
using the Imputer function
parameter : missing_values, strategy, axis and we are filling
Filling the missing value by mean means into the dataSet
"""
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values= 'NaN', strategy= 'mean', axis= 0) 

"""
Replacing the missing values by the mean value
"""

imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])


"""
Encoding categorical data
putting the dataset into categories
"""
from sklearn.preprocessing import LabelEnconder, OneHotEncoder
labelencoder_X = LabelEncoder()
labelencoder_X.fit_transform()







