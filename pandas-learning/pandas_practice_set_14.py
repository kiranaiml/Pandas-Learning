"""
1. Print both DataFrames.

2. Concatenate both DataFrames vertically.

3. Print the concatenated DataFrame.

4. Print its shape.

5. Reset the index.

6. Add a Bonus column (10% of Salary).

7. Sort by Salary (highest to lowest).

8. Print the employee with the highest Salary.

9. Save as "concat_data.csv" without the index.

10. Read the CSV and print it.
"""
import pandas as pd

data1 = {
    "Name": ["Kiran", "Rahul", "Anjali"],
    "Salary": [25000, 40000, 35000]
}

data2 = {
    "Name": ["Priya", "Vikram", "Sneha"],
    "Salary": [28000, 50000, 42000]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
print(df1)
print(df2)
data=pd.concat([df1,df2],axis=0)
print(data)
print(data.shape)
data=pd.concat([df1,df2],ignore_index=True)
data["Bonus"]=data["Salary"]*0.10
data.sort_values(by="Salary",ascending=False,inplace=True)
print(data[data["Salary"]==data["Salary"].max()])
data.to_csv("concat_data.csv",index=False)
print(pd.read_csv("concat_data.csv"))