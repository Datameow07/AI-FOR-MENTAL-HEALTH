# -*- coding: utf-8 -*-
"""LGHC_dtc_rfc.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t-6l91UoRI4-1lOAdb38liwxNeoK6mRQ
"""

# This indicator is based on the question: "“Has a doctor, nurse or other health
# professional EVER told you that you have a depressive disorder (including depression,
# major depression, dysthymia, or minor depression)?”

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import KFold, cross_val_score, train_test_split
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import keras
from keras.layers import Dense
import tensorflow as tf
from keras import layers, models

df = pd.read_csv('/Users/arbiazabi/WEB DEVELOPMENT 5TH SEM/react-cycle1/frontend mental/Psykh-A-Mental-Health-Chatbot/frontend mental 2/MindEase/database/adult-depression-lghc-indicator-2.csv')

df.info()

df.head()

import keras
from keras.models import Sequential
from keras.layers import Dense
# Drop rows not necessary for model
df = df.drop(['Strata','Strata Name', 'Year','Frequency'], axis=1)
# Drop rows with NaN values
df.dropna(inplace=True)
df.head()

# Labelencoding 
labelencoder = LabelEncoder()
df['Lower 95% CL'] = labelencoder.fit_transform(df['Lower 95% CL'])
df['Upper 95% CL'] = labelencoder.fit_transform(df['Upper 95% CL'])

# Splitting DS into test and train
X = df.drop(['Upper 95% CL'], axis=1)
y = df['Upper 95% CL']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate the model on the testing set
score = model.score(X_test, y_test)
print("Model accuracy:", score)
