"""
Tasks (No Answers)
Create a new column called Bonus equal to 10% of Salary.
Create a new column called Tax equal to 5% of Salary.
Update Salary by adding 2000 to every employee.
Update Age by adding 1 year to everyone.
Drop the Tax column.
Drop the Bonus column using inplace=True.
Drop the row with index 0.
Drop the row with index 2 using inplace=True.
Print the shape before dropping rows.
Print the shape after dropping rows.
Create a column called YearlySalary.
Drop both Age and City columns together.
Check the remaining columns.
Create a new column called NetSalary = Salary - 1000.
Print the final DataFrame.
Challenge Questions
Drop the employee with the highest salary.
Drop the employee with the lowest salary.
Create a column called SalaryCategory:
"High" if Salary > 40000
"Low" otherwise"""
import pandas as pd

data = {
    "Name": ["Kiran", "Rahul", "Anjali", "Priya", "Vikram"],
    "Age": [18, 22, 21, 19, 25],
    "City": ["Hassan", "Mysore", "Hassan", "Bangalore", "Mysore"],
    "Salary": [25000, 40000, 35000, 28000, 50000]
}

df = pd.DataFrame(data)

print(df.shape)
df["Bonus"] = df["Salary"] * 0.10
df["Tax"] = df["Salary"] * 0.05
df["Salary"] = df["Salary"] + 2000
df["Age"] = df["Age"] + 1
df.drop(columns=["Tax"], inplace=True)
df.drop(columns=["Bonus"], inplace=True)
df.drop(0, inplace=True)
df.drop(2, inplace=True)
print(df.shape)
df["YearlySalary"] = df["Salary"] * 12
df.drop(columns=["Age", "City"], inplace=True)
print(df.columns)
df["NetSalary"] = df["Salary"] - 1000
highest_index = df["Salary"].idxmax()
df.drop(highest_index, inplace=True)

lowest_index = df["Salary"].idxmin()
df.drop(lowest_index, inplace=True)
df["SalaryCategory"] = ["High" if x > 40000 else "Low" for x in df["Salary"]]

print(df)