"""
Print first 3 rows.
Print last 2 rows.
Print only Name and Salary.
Print all people from Hassan.
Print all people whose Salary is above 35000.
Print maximum Salary.
Print minimum Age.
Print average Salary.
Print unique cities.
Count total rows.
Sort Salary from highest to lowest.
Create a new column Bonus = Salary * 0.10.
Print people whose Age is greater than 20 and City is Hassan.
Print names only from Bangalore.
Print second highest Salary.

"""
import pandas as pd

data = {
    "Name": ["Kiran", "Rahul", "Anjali", "Priya", "Vikram", "Sneha", "Arjun", "Pooja"],
    "Age": [18, 22, 21, 19, 25, 23, 20, 24],
    "City": ["Hassan", "Mysore", "Hassan", "Bangalore", "Mysore", "Hassan", "Bangalore", "Hassan"],
    "Salary": [25000, 40000, 35000, 28000, 50000, 42000, 30000, 45000]
}

df = pd.DataFrame(data)
print(df.head(3))
print(df.tail(2))
print(df[["Name","Salary"]])
print(df["City"]=="Hassan")
print(df["Salary"]>35000)
print(df["Salary"].max())
print(df["Salary"].min())
print(df["Salary"].mean())
print(df["City"].unique())
print(df.shape[0])
print(df.sort_values("Salary",ascending=False))
df["Bonus"]=df["Salary"]*0.10
print((df["Age"]>20) & (df["City"]=="Hassan"))
print(df[df["City"] == "Bangalore"]["Name"])
print(df["Salary"].sort_values(ascending=False).iloc[1])