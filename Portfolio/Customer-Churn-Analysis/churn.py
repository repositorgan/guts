import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('dataset.csv')
sns.barplot(data=df, x='churn', y='tenure')
plt.show()
