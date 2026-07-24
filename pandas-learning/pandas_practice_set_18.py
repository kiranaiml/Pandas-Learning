"""
1. Create a pivot table to find the average Salary for each Department.

2. Create a pivot table to find the maximum Salary for each Department.

3. Create a pivot table to find the minimum Salary for each Department.

4. Create a pivot table to find the total Salary for each Department.

5. Create a pivot table to count how many employees are in each Department.

6. Create a pivot table with:
   Index = Department
   Values = Age
   aggfunc = mean

7. Create a pivot table with:
   Index = City
   Values = Salary
   aggfunc = mean

8. Create a pivot table with:
   Index = City
   Values = Age
   aggfunc = max

9. Create a pivot table with:
   Index = Department
   Values = Salary
   aggfunc = median

10. Create a pivot table to find the first Salary in each Department.
"""
import pandas as pd

data = {
    "Name": [
        "Kiran", "Rahul", "Anjali", "Priya", "Vikram",
        "Sneha", "Arjun", "Pooja", "Rohit", "Meena"
    ],
    "Age": [21, 25, 22, 24, 28, 23, 26, 27, 24, 22],
    "Gender": [
        "Male", "Male", "Female", "Female", "Male",
        "Female", "Male", "Female", "Male", "Female"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance", "HR",
        "Finance", "IT", "HR", "Finance", "IT"
    ],
    "City": [
        "Bangalore", "Mysore", "Hassan", "Bangalore", "Mysore",
        "Hassan", "Bangalore", "Mysore", "Hassan", "Bangalore"
    ],
    "Salary": [
        45000, 52000, 38000, 47000, 60000,
        42000, 55000, 50000, 48000, 43000
    ],
    "Bonus": [
        5000, 7000, 4000, 5000, 8000,
        4500, 6500, 6000, 5500, 4500
    ]
}

df = pd.DataFrame(data)

print(df)
df.pivot_table(values="Salary",index="Department",aggfunc="mean")
print(df)
df.pivot_table(values="Salary",index="Department",aggfunc="max")
print(df)
df.pivot_table(values="Salary",index="Department",aggfunc="min")
print(df)
df.pivot_table(values="Salary",index="Department",aggfunc="sum")
print(df)
print(df.pivot_table(values="Name", index="Department", aggfunc="count"))
print(df)
df.pivot_table(values="Age",index="Department",aggfunc="mean")
print(df)
df.pivot_table(values="Salary",index="City",aggfunc="mean")
print(df)
df.pivot_table(values="Age",index="City",aggfunc="max")
print(df)
df.pivot_table(values="Salary",index="Department",aggfunc="median")
print(df)
df.pivot_table(values="Salary",index="Department",aggfunc="first")
print(df)
