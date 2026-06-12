"""
# Task 1
# Print the first 4 rows

# Task 2
# Print the last 3 rows

# Task 3
# Find how many rows and columns are present

# Task 4
# Print all column names

# Task 5
# Print only the Age column

# Task 6
# Print only the Salary column

# Task 7
# Print the third row using iloc

# Task 8
# Print rows 2 to 6 using iloc

# Task 9
# Print only Name and City columns

# Task 10
# Print the first 5 names

# Task 11
# Find the highest salary

# Task 12
# Find the lowest salary

# Task 13
# Find the average age

# Task 14
# Count total employees

# Task 15
# Find all unique cities

# Task 16
# Show employees whose age is greater than 21

# Task 17
# Show employees from Hassan

# Task 18
# Show employees from Hassan OR Mysore

# Task 19
# Show employees whose salary is greater than 35000

# Task 20
# Sort employees by salary from highest to lowest

# Bonus 1
# Create a new column called Bonus equal to 10% of Salary

# Bonus 2
# Create a new column called Tax equal to 5% of Salary

# Bonus 3
# Print only employees whose Bonus is greater than 4000

# Bonus 4
# Find the city that appears most frequently

# Bonus 5
# Sort employees by Age from youngest to oldest
"""
import pandas as pd

data = {
    "Name": ["Kiran", "Rahul", "Anjali", "Priya", "Vikram", "Sneha", "Arjun", "Pooja"],
    "Age": [18, 22, 21, 19, 25, 23, 20, 24],
    "City": ["Hassan", "Mysore", "Hassan", "Bangalore", "Mysore", "Hassan", "Bangalore", "Hassan"],
    "Salary": [25000, 40000, 35000, 28000, 50000, 42000, 30000, 45000]
}

df = pd.DataFrame(data)
print(df.iloc[0])
print(df.tail(3))
print(df.shape)
print(df.columns)
print(df["Age"])
print(df["Salary"])
print(df.iloc[2])
print(df.iloc[1:7])
print(df[["Name","City"]])
print(df["Name"].iloc[0:5])
print(df["Salary"].max())
print(df["Salary"].min())
print(df["Age"].mean())
print(df["Name"].count())
print(df["City"].unique())
print(df["Age"]>21)
print(df["City"]=="Hassan")
print((df["City"]=="Hassan") | (df["City"]=="Mysore"))
print(df["Salary"]>35000)
print(df.sort_values("Salary",ascending=False))
df["Bouns"]=df["Salary"]*0.10
print(df)
df["Tax"]=df["Salary"]*0.05
print(df)
print(df["Bouns"]>4000)
print(df["City"].mode())
print(df.sort_values("Age",ascending=True))