# -*- coding: utf-8 -*-
"""Task3CodSoft.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XymvLgnkSnERBLpaZdjb-lSuhxEnzBr5
"""

##TASK-2 : IRIS FLOWER CLASSIFICATION

##Author : AMAR SHEWALKAR

##Batch : 01 JULY 2024 TO 31 JULY 2024

##Domain : Data science

##Aim : to develop a model that can classify iris flowers into different species based on their sepal and petal measurements.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris = pd.read_csv("/content/IRIS.csv")

iris.shape

iris.head()

iris.isnull().sum()

iris.info()

iris['species'].value_counts()

iris.describe()

iris.groupby('species').mean()

sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species')
plt.title('Sepal Length vs Sepal Width')

sns.scatterplot(data=iris, x='petal_length', y='petal_width', hue='species')
plt.title('Patel Length vs Patel Width')

iris['species'] = iris['species'].map({'Iris-setosa':1, 'Iris-versicolor':2, 'Iris-virginica':3})

iris.corr()

type(iris.corr())

iris.corr()['species']

iris.corr()['species'].drop('species')

iris_df = iris.drop(columns='sepal_width', axis=1)

sns.scatterplot(data=iris_df, x='sepal_length', y='petal_length', hue='species')

iris_df.head()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

X = iris_df.drop(columns='species', axis=1)
y = iris_df['species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=2, stratify=y)

print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

logistic_model = LogisticRegression()

logistic_model.fit(X_train, y_train)

decision_model = DecisionTreeClassifier()

decision_model.fit(X_train, y_train)

y_train_logistic_predicted = logistic_model.predict(X_train)
acc1 = accuracy_score(y_train, y_train_logistic_predicted)
acc1

y_test_logistic_predicted = logistic_model.predict(X_test)
acc2 = accuracy_score(y_test, y_test_logistic_predicted)
acc2

y_train_tree_predicted = decision_model.predict(X_train)
acc3 = accuracy_score(y_train, y_train_tree_predicted)
acc3

y_test_tree_predicted = decision_model.predict(X_test)
acc4 = accuracy_score(y_test, y_test_tree_predicted)
acc4