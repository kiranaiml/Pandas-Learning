"""
Pandas Practice Set 10 - Revision

1. Print the DataFrame.

2. Print the number of missing values in each column.

3. Print the total number of missing values in the DataFrame.

4. Print only the rows that contain at least one missing value.

5. Replace missing Salary values with 0.

6. Replace missing Age values with the average Age.

7. Replace missing City values with "Unknown".

8. Check whether any missing values are left.

9. Print the average Salary after filling missing values.

10. Print the highest Salary.

11. Print employees whose Salary is greater than 40000.

12. Count employees in each City.

13. Add a new column named Bonus = 10% of Salary.

14. Remove rows where Salary is 0.

15. Reset the index.

16. Save the cleaned DataFrame as "employees_clean.csv" without the index.

17. Read "employees_clean.csv" and print it.

18. Print the DataFrame shape.

19. Print all column names.

20. Print the employee with the highest Salary.
"""
import pandas as pd

data = {
    "Name": ["Kiran", "Rahul", "Anjali", "Priya", "Vikram", "Sneha", "Arjun", "Pooja", "Rohit", "Neha"],
    "Age": [18, 22, None, 19, 25, 23, 20, None, 27, 26],
    "City": ["Hassan", "Mysore", "Hassan", None, "Mysore",
             "Hassan", "Bangalore", "Hassan", "Mysore", "Bangalore"],
    "Salary": [25000, 40000, 35000, None, 50000,
               42000, 30000, 45000, None, 48000]
}

df = pd.DataFrame(data)

print(df)
print(df.isna())
print(df.isna().sum())
print(df["Age"].iloc[2])
print(df["Salary"].fillna(0))
print(df["Salary"].max())
print(df[df["Salary"]>40000][["Name"]])
print(df.groupby("City")["Name"].count())
df["Bonus"]=df["Salary"]*0.10
df.dropna()
df.reset_index()
df.to_csv("employee_cleandata.csv")
pd.read_csv("employee_cleandata.csv")
print(df.shape)
print(df.columns)
print(df[df["Salary"]==df["Salary"].max()]["Name"])