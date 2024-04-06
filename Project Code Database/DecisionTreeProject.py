#!/usr/bin/env python
# coding: utf-8
import pandas as pd
moistureData = pd.read_csv('output.csv')
moistureData
X = moistureData.drop(columns=['Condition'])
X = X.drop(columns=['year'])
X = X.drop(columns=['month'])
X = X.drop(columns=['day'])
X = X.drop(columns=['hour'])
X = X.drop(columns=['minute'])
X = X.drop(columns=['second'])
y = moistureData['Condition']
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(X.values, y.values) #Takes two things input set and output set
a = float(input("Enter moist"))
predictions = model.predict([[a]]) #This takes input as an array
print(predictions)
from sklearn.model_selection import train_test_split
#Now we give 3 arguments to train_test_split() functions as X, y and split
X_train , X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2) #This function return tuple so we can unpack it into 4 varibles
model = DecisionTreeClassifier()
model.fit(X_train.values, y_train.values)
predictions = model.predict(X_test.values) 
from sklearn.metrics import accuracy_score
score = accuracy_score(y_test, predictions)
print("Model Accuracy:", score*100,"%")
import joblib
joblib.dump(model, 'DecisionTree.joblib')