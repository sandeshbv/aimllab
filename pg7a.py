# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 09:51:38 2022

@author: admin
"""
from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
iris = datasets.load_iris()
x = pd.DataFrame(iris.data)
x.columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']
y = pd.DataFrame(iris.target)
y.columns = ['Targets']
plt.figure(figsize = (14, 7))
colormap = np.array(['red', 'lime', 'black'])
plt.subplot(1, 2, 1)
plt.scatter(x.Sepal_Length, x.Sepal_Width, c = colormap[y.Targets], s = 40)
plt.title('Sepal')

plt.subplot(1, 2, 2)
plt.scatter(x.Petal_Length, x.Petal_Width, c = colormap[y.Targets], s = 40)
plt.title('Petal')
model = KMeans(n_clusters = 3)
model.fit(x)
plt.figure(figsize = (14, 7))
colormap = np.array(['red', 'lime', 'black'])
plt.subplot(1, 2, 1)
plt.scatter(x.Petal_Length, x.Petal_Width, c = colormap[y.Targets], s = 40)
plt.title('Real')
plt.subplot(1, 2, 1)
plt.scatter(x.Petal_Length, x.Petal_Width, c = colormap[model.labels_], s = 40)
plt.title('KMeans')
print('Accuracy score', accuracy_score(y.Targets, model.labels_))
print('Confusion matrix', confusion_matrix(y.Targets, model.labels_))