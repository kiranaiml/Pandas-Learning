import pandas as pd
data=pd.read_json('sample_Data.json')
print('first 10 data')
print(data.head(10))
print('Last 10 data')
print(data.tail(10))