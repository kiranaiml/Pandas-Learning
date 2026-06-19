"""
Task Set 2
Create a column YearlySalary.
Create a column Bonus = 15% of salary.
Find total yearly salary of all employees.
Find employee with highest salary.
Find employee with lowest salary.
Print only Name and NetSalary.
Count employees whose salary is above 35000.
Print all employees sorted by city.
Print all employees sorted by age descending.
Find number of unique cities.
"""
import pandas as pd

data = {
    "Name": ["Kiran", "Rahul", "Anjali", "Priya", "Vikram", "Sneha", "Arjun", "Pooja"],
    "Age": [18, 22, 21, 19, 25, 23, 20, 24],
    "City": ["Hassan", "Mysore", "Hassan", "Bangalore", "Mysore", "Hassan", "Bangalore", "Hassan"],
    "Salary": [25000, 40000, 35000, 28000, 50000, 42000, 30000, 45000]
}

df = pd.DataFrame(data)
df["YearlySalary"]=None
df["Bonus"] = df["Salary"] * 0.15
df["YearlySalary"] = df["Salary"] * 12
print(df[df["Salary"] == df["Salary"].max()])
print(df[df["Salary"] == df["Salary"].min()])
print(df[["Name","YearlySalary"]])
print((df["Salary"] > 35000).sum())
print(df.sort_values("City"))
print(df.sort_values("Age", ascending=False))
print(df["City"].nunique())