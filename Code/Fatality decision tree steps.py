#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('dataset_merged.csv')
df['high_impact'] = df['number_of_fatalities'].apply(lambda x: 0 if x == 1 else 1)

# Using Decision Tree and Logistic Regression 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.tree import plot_tree

target = df['high_impact']

df.drop(['high_impact', 'number_of_fatalities'], axis = 1, inplace = True)

features_column = ['type','month', 'day', 'hour', 'time', 'speeding', 'ran_red_light', 'dl_status', 'suspected_impairment',
       'restraint_type', 'type_of_road', 'ftsra']

features = df[features_column]

features = pd.get_dummies(features)

# Assuming 'target' is the target variable you want to predict

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Decision Tree
dt_model = DecisionTreeClassifier()
dt = dt_model.fit(X_train, y_train)
dt_predictions = dt_model.predict(X_test)
dt_accuracy = accuracy_score(y_test, dt_predictions)
print("Decision Tree Accuracy:", dt_accuracy)
print("Decision Tree Classification Report:\n", classification_report(y_test, dt_predictions))

# Logistic Regression
lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)
lr_predictions = lr_model.predict(X_test)
lr_accuracy = accuracy_score(y_test, lr_predictions)
print("Logistic Regression Accuracy:", lr_accuracy)
print("Logistic Regression Classification Report:\n", classification_report(y_test, lr_predictions))

# Displaying Decision Tree
plt.figure(figsize = (90,80)) #make it bigger
plot_tree(dt, feature_names=features.columns)

