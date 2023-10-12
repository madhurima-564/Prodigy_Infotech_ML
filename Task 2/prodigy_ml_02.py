# -*- coding: utf-8 -*-
"""PRODIGY_ML_02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18aToHJOswHmVAyQbkLSVBNyzspCrb5uq

**Importing the Dependencies**
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans

import plotly.graph_objs as go
import plotly.offline as pyo

"""**Data Collection & Analysis**"""

df = pd.read_csv("Mall_Customers.csv")
df

df.shape

df.describe()

df.info()

df.columns

df.isnull().sum()

sns.displot(df["Age"])

sns.displot(df["Annual Income (k$)"])

sns.displot(df["Spending Score (1-100)"])

df.plot(kind = "scatter", x = "Annual Income (k$)", y = "Spending Score (1-100)", figsize=(10,7))
plt.show()

X = df.iloc[:, [3,4]].values
X

"""**Choosing Number of Clusters**"""

wcss = []
for i in range(1,11):
  kmeans = KMeans(n_clusters = i,init = 'k-means++',random_state = 42)
  kmeans.fit(X)
  wcss.append(kmeans.inertia_)

sns.set()
plt.plot(range(1,11), wcss)
plt.title("The Elbow Point Graph")
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

"""**Training the K-means Clustering model**"""

kmeans = KMeans(n_clusters = 5, init='k-means++', random_state = 0)
Y = kmeans.fit_predict(X)
print(Y)

print("Centroids", kmeans.cluster_centers_)

centroids = kmeans.cluster_centers_

"""**2D Visualization of Clusters**"""

plt.figure(figsize =(10,7))
plt.scatter(X[Y==0,0], X[Y==0,1], s=20,color ='green', label='Cluster 1')
plt.scatter(X[Y==1,0], X[Y==1,1], s=20,color ='violet', label='Cluster 2')
plt.scatter(X[Y==2,0], X[Y==2,1], s=20,color ='red', label='Cluster 3')
plt.scatter(X[Y==3,0], X[Y==3,1], s=20,color ='blue', label='Cluster 4')
plt.scatter(X[Y==4,0], X[Y==4,1], s=20,color ='black', label='Cluster 5')

plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s = 50, c='cyan', label ='Centroids')
plt.title("Customer Groups")
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score(1-100)')
plt.legend()
plt.show()

"""**3D Visualization**"""

labels = kmeans.labels_

cluster_colors = ['green', 'violet', 'red', 'blue', 'black']

df['Cluster'] = labels

fig = go.Figure()

for cluster_label, color in zip(range(5), cluster_colors):
    cluster_data = df[df['Cluster'] == cluster_label]
    fig.add_trace(go.Scatter3d(
        x=cluster_data['Annual Income (k$)'],
        y=cluster_data['Spending Score (1-100)'],
        z=cluster_data['Age'],
        mode='markers',
        name=f'Cluster {cluster_label}',
        marker=dict(size=5, color=color)
    ))

fig.update_layout(
    scene=dict(
        xaxis_title='Annual Income (k$)',
        yaxis_title='Spending Score (1-100)',
        zaxis_title='Age'
    ),
    title="K-means Clustering of Mall Customers"
)

pyo.iplot(fig)