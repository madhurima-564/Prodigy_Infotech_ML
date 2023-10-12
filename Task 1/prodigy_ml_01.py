# -*- coding: utf-8 -*-
"""PRODIGY_ML_01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ANSZlIl665KfcHbD0OrClvqp2t58OcOE
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('train.csv')
df

print(df.info())

df.columns

df.describe()

correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

df['Bathrooms'] = df['FullBath'] + 0.5 * df['HalfBath']

fig, axs = plt.subplots(2,4, figsize = (10,5))

plt1 = sns.boxplot(df['Bathrooms'], ax = axs[0,0])
plt2 = sns.boxplot(df['LotArea'], ax = axs[0,1])
plt3 = sns.boxplot(df['GrLivArea'], ax = axs[0,2])
plt4 = sns.boxplot(df['BedroomAbvGr'], ax = axs[0,3])
plt5 = sns.boxplot(df['SalePrice'], ax = axs[1,1])

plt.tight_layout()

# FOR PRICE
plt.boxplot(df.SalePrice)
Q1 = df.SalePrice.quantile(0.25)
Q3 = df.SalePrice.quantile(0.75)
IQR = Q3 - Q1
df = df[(df.SalePrice >= Q1 - 1.5*IQR) & (df.SalePrice <= Q3 + 1.5*IQR)]

# FOR LOTAREA
plt.boxplot(df.LotArea)
Q1 = df.LotArea.quantile(0.25)
Q3 = df.LotArea.quantile(0.75)
IQR = Q3 - Q1
df = df[(df.LotArea>= Q1 - 1.5*IQR) & (df.LotArea <= Q3 + 1.5*IQR)]

# FOR GRLIVAREA
plt.boxplot(df.GrLivArea)
Q1 = df.GrLivArea.quantile(0.25)
Q3 = df.GrLivArea.quantile(0.75)
IQR = Q3 - Q1
df = df[(df.GrLivArea >= Q1 - 1.5*IQR) & (df.GrLivArea <= Q3 + 1.5*IQR)]

# FOR BEDROOM
plt.boxplot(df.BedroomAbvGr)
Q1 = df.BedroomAbvGr.quantile(0.25)
Q3 = df.BedroomAbvGr.quantile(0.75)
IQR = Q3 - Q1
df = df[(df.BedroomAbvGr >= Q1 - 1.5*IQR) & (df.BedroomAbvGr <= Q3 + 1.5*IQR)]

#RE-ANALYSIS
fig, axs = plt.subplots(2,4, figsize = (10,5))

plt1 = sns.boxplot(df['Bathrooms'], ax = axs[0,0])
plt2 = sns.boxplot(df['LotArea'], ax = axs[0,1])
plt3 = sns.boxplot(df['GrLivArea'], ax = axs[0,2])
plt4 = sns.boxplot(df['BedroomAbvGr'], ax = axs[0,3])
plt5 = sns.boxplot(df['SalePrice'], ax = axs[1,1])

plt.tight_layout()

columns = ['LotArea','GrLivArea', 'BedroomAbvGr', 'Bathrooms', 'SalePrice']
df = df[columns]
print(df)

X = df[['LotArea','GrLivArea', 'BedroomAbvGr', 'Bathrooms']]
y = df['SalePrice']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(X_train,y_train)

y_pred = lr.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R-squared:", r2)

plt.scatter(y_test, y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual Prices vs. Predicted Prices")
plt.show()

residuals = y_test - y_pred
plt.scatter(y_test, residuals)
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel("Actual Prices")
plt.ylabel("Residuals")
plt.title("Residual Plot")
plt.show()

sns.displot((y_test-y_pred), bins=50)

d = pd.read_csv("test.csv")
d

d['Bathrooms'] = d['FullBath'] + 0.5 * d['HalfBath']

X_test = d[['LotArea','GrLivArea', 'BedroomAbvGr', 'Bathrooms']]

predicted_prices = lr.predict(X_test)

d['Predicted_Price'] = predicted_prices
d

columns = ['LotArea','GrLivArea', 'BedroomAbvGr', 'Bathrooms', 'Predicted_Price']
d = d[columns]
print(d)

fig = plt.figure()
plt.scatter(y_test,y_pred)
fig.suptitle('y_test vs y_pred')
plt.xlabel('y_test')
plt.ylabel('y_pred')

r2 = r2_score(y_test, y_pred)
print(f"R-squared (R2) value: {r2}")

pd.DataFrame(d).to_csv("Predictions.csv", index=True)