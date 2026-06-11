

# Task 1
# Show only people with Age > 20 and Salary > 35000


# Task 2
# Find:
# Highest salary
# Lowest salary
# Average salary


# Task 3
# Show all employees from Hassan
# Sort them by Salary from highest to lowest


# Task 4
# Create a new column:
# Bonus = Salary * 0.10
# Print Name, Salary, Bonus

# Task 5
# Count how many people belong to each City


# Bonus Challenge
# Find the name of the employee with the highest salary
# WITHOUT using .max()
import pandas as pd

data = {
    "Name": ["Kiran", "Rahul", "Anjali", "Priya", "Vikram", "Sneha", "Arjun", "Pooja"],
    "Age": [18, 22, 21, 19, 25, 23, 20, 24],
    "City": ["Hassan", "Mysore", "Hassan", "Bangalore", "Mysore", "Hassan", "Bangalore", "Hassan"],
    "Salary": [25000, 40000, 35000, 28000, 50000, 42000, 30000, 45000]
}

df = pd.DataFrame(data)
print(df[(df["Age"] > 20) & (df["Salary"] > 35000)])
print(df["Salary"].max())
print(df["Salary"].min())
print(df["Salary"].mean())
print(
    df[df["City"]=="Hassan"]
      .sort_values("Salary", ascending=False)
)
df["Bonus"]=df["Salary"]*0.10
print(df[["Name","Salary","Bonus"]])
print(df["City"].count())
print(
    df.sort_values("Salary", ascending=False)
      .iloc[0]["Name"]
)