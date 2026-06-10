"""

Task 1
Print the first 5 rows.
Task 2
Print the last 3 rows.
Task 3
Print the DataFrame shape.
Task 4
Print all column names.
Task 5
Print only the Name column.
Task 6
Print only the Age column.
Task 7
Print only the City column.
Task 8
Print the first row.
Task 9
Print rows 2 to 5.
Task 10
Find the maximum age.
Task 11
Find the minimum age.
Task 12
Find the average age.
Task 13
Show people whose age is greater than 20.
Task 14
Show people whose city is "Hassan".
Task 15
Sort the DataFrame by age (smallest to largest).
Task 16
Sort the DataFrame by age (largest to smallest).
Task 17
Add this Salary column:
[25000, 30000, 28000, 35000, 26000, 40000, 32000, 45000, 29000, 38000]
Task 18
Find the highest salary.
Task 19
Count total number of people.
Task 20
Find total unique cities.
"""

import pandas as pd

data = {
    "Name": ["Kiran", "Rahul", "Priya", "Amit", "Sneha", "Ravi", "Anjali", "Vijay", "Pooja", "Arjun"],
    "Age": [18, 21, 20, 22, 19, 23, 21, 24, 20, 22],
    "City": ["Hassan", "Bengaluru", "Mysuru", "Mangaluru", "Hubballi", "Belagavi", "Shivamogga", "Davanagere", "Tumakuru", "Udupi"]
}

df = pd.DataFrame(data)

print(df)
print(df.head(5))
print(df.tail(3))
print(df.shape)
print(df.columns)
print(df.Name)
print(df["Age"])
print(df["City"])
print(df.iloc[0])
print(df.iloc[1:6])
print(df["Age"].max())
print(df["Age"].min())
print(df["Age"].mean())
print(df["Age"]>20)
print(df["City"]=="Hassan")
print(df.sort_values("Age"))
print(df.sort_values("Age",ascending=False))
df["Salary"]=df["Age"]*2000
print(df["Salary"])
print(df["Salary"].max())
print(df["Name"].count())
print(df["City"].unique())