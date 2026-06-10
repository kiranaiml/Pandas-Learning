import pandas as pd
data=pd.read_json('/Users/kiranlm/pandas-learning/sample_Data.json')
print("Frist 10 list of data")
print(data.head(10))
print("Last 10 list of data")
print(data.tail(10))