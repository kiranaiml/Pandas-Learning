"""
Print employees whose age is greater than 21.
Print employees from Hassan with salary greater than 30000.
Count employees in each city.
Find average age city-wise.
Find total salary city-wise.
Find highest age city-wise.
Find lowest salary city-wise.
Print top 3 highest-paid employees.
Print top 2 youngest employees.
Create a column called NetSalary = Salary - 2000.
"""
import pandas as pd

data = {
    "Name": ["Kiran", "Rahul", "Anjali", "Priya", "Vikram", "Sneha", "Arjun", "Pooja"],
    "Age": [18, 22, 21, 19, 25, 23, 20, 24],
    "City": ["Hassan", "Mysore", "Hassan", "Bangalore", "Mysore", "Hassan", "Bangalore", "Hassan"],
    "Salary": [25000, 40000, 35000, 28000, 50000, 42000, 30000, 45000]
}

df = pd.DataFrame(data)
print(df[df["Age"]>21])
print(df[(df["City"]=="Hassan") & (df["Salary"]>30000)])
print(df.groupby("City")["Name"].count())
print(df.groupby("City")["Age"].mean())
print(df.groupby("City")["Salary"].sum())
print(df.groupby("City")["Age"].max())
print(df.groupby("City")["Salary"].min())
data=df.sort_values("Salary",ascending=False)
print(data.head(3))
data1=df.sort_values("Age",ascending=True)
print(data1.head(2))
df["Net Salary"]=df["Salary"]-2000
print(df)