from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from joblib import dump


data = load_iris()
model = DecisionTreeClassifier().fit(data.data, data.target)
dump(model, 'model.joblib')
