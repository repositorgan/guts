import pandas as pd

def load_data():
return pd.DataFrame({
'metric': ['Revenue', 'Users', 'Churn'],
'value': [12000, 530, 7]
})
