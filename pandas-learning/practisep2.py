"""
Print the DataFrame.
Find the average salary city-wise.
Find the maximum salary city-wise.
Find the minimum salary city-wise.
Count how many people are in each city.
Find the total salary city-wise.
Sort cities by total salary (highest first).
Find which city has the highest average salary.
Print only the salary column grouped by city.
Find the number of unique cities.
"""
import pandas as pd

data = {
    "Name": ["Kiran", "Rahul", "Anjali", "Priya", "Vikram", "Sneha", "Arjun", "Pooja"],
    "City": ["Hassan", "Mysore", "Hassan", "Bangalore", "Mysore", "Hassan", "Bangalore", "Hassan"],
    "Salary": [25000, 40000, 35000, 28000, 50000, 42000, 30000, 45000]
}

df = pd.DataFrame(data)
print(df)
print(df.groupby("City")["Salary"].mean())
print(df.groupby("City")["Salary"].max())
print(df.groupby("City")["Salary"].min())