import pandas as pd
from sklearn.linear_model import LinearRegression


sales = pd.read_csv('data.csv')
X = sales[['month']]
y = sales['revenue']


model = LinearRegression().fit(X, y)
print("Next month forecast:", model.predict([[13]])[0])
