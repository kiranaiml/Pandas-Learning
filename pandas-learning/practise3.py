
# Task 1
# Show only Name and Salary columns.

# Task 2
# Show employees whose City is Hassan OR Mysore.

# Task 3
# Find all employees whose Salary is between 30000 and 45000.

# Task 4
# Create a new column:
# Tax = Salary * 0.05

# Task 5
# Print only employees whose Age is greater than the average Age.

# Task 6
# Find how many unique cities are present.

# Task 7
# Sort by:
# 1. City (A to Z)
# 2. Salary (Highest to Lowest)

# Bonus ⭐
# Find the second highest salary person's Name.
# Do not manually type the name.
import pandas as pd

data = {
    "Name": ["Kiran", "Rahul", "Anjali", "Priya", "Vikram", "Sneha", "Arjun", "Pooja"],
    "Age": [18, 22, 21, 19, 25, 23, 20, 24],
    "City": ["Hassan", "Mysore", "Hassan", "Bangalore", "Mysore", "Hassan", "Bangalore", "Hassan"],
    "Salary": [25000, 40000, 35000, 28000, 50000, 42000, 30000, 45000]
}

df = pd.DataFrame(data)
print(df[["Name","Salary"]])
print(df[(df["City"]=="Hassan") | (df["City"]=="Mysore")]["Name"])
print(df[df["Salary"].between(30000,45000)]["Name"])
df["Tax"]=df["Salary"]*0.05
print(df[df["Age"] > df["Age"].mean()]["Name"])
print(df["City"].nunique())
print(df.sort_values(["City", "Salary"], ascending=[True, False]))
print(df.sort_values("Salary", ascending=False).iloc[1]["Name"])