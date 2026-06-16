import pandas as pd

data = {
    "Name": ["Kiran", "Rahul", "Anjali", "Priya", "Vikram", "Sneha", "Arjun", "Pooja"],
    "Age": [18, 22, 21, 19, 25, 23, 20, 24],
    "City": ["Hassan", "Mysore", "Hassan", "Bangalore", "Mysore", "Hassan", "Bangalore", "Hassan"],
    "Salary": [25000, 40000, 35000, 28000, 50000, 42000, 30000, 45000]
}

df = pd.DataFrame(data)

# Task 1
# Print total salary of all employees

# Task 2
# Print number of employees

# Task 3
# Print median salary

# Task 4
# Show employees whose salary is greater than 35000

# Task 5
# Show employees whose age is greater than 21

# Task 6
# Show employees from Hassan

# Task 7
# Show employees from Bangalore

# Task 8
# Find total salary city-wise

# Task 9
# Find average age city-wise

# Task 10
# Find maximum salary city-wise

# Task 11
# Find minimum salary city-wise

# Task 12
# Sort data by Name

# Task 13
# Sort data by Salary (high to low)

# Task 14
# Create a new column Bonus = Salary * 0.2

# Task 15
# Create a new column Tax = Salary * 0.1

# Task 16
# Print only Name and Bonus columns

# Task 17
# Print only Name, City and Salary columns

# Task 18
# Count employees city-wise

# Task 19
# Print unique cities

# Task 20
# Print total number of unique cities
print(df["Salary"].sum())
print(df["Name"].count())
print(df["Salary"].median())
print(df["Salary"]>35000)
print(df["Age"]>21)
print(df["City"]=="Hassan")
print(df["City"]=="Bangalore")
print(df.groupby("City")["Salary"].sum())
print(df.groupby("City")["Salary"].mean())
print(df.groupby("City")["Salary"].max())
print(df.groupby("City")["Salary"].min())
print(df.sort_values("Name",ascending=True))
print(df.sort_values("Salary",ascending=False))
df["Bonus"]=df["Salary"]*0.2
df["Tax"]=df["Salary"]*0.1
print(df[["Name","Bonus"]])
print(df[["Name","City","Salary"]])
print(df.groupby("City")["Name"].count())
print(df["City"].unique())
print(df.count()["City"].unique())