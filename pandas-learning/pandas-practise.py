"""
Pandas Practice - Level 8

1. Print employees whose Salary is greater than 40000.

2. Print employees whose Age is between 20 and 25 (inclusive).

3. Print only the Name and Salary columns of employees from Hassan.

4. Find the second highest Salary.

5. Find the third highest Salary.

6. Print the employee(s) with the highest Salary.

7. Print the employee(s) with the lowest Salary.

8. Count the number of employees in each City.

9. Find the average Age for each City.

10. Find the total Salary for each City.

11. Add a new column named Experience with the value 1 for all employees.

12. Increase every employee's Salary by 5%.

13. Create a new column named MonthlyTax equal to 8% of Salary.

14. Remove the Experience column.

15. Sort the DataFrame by City (ascending) and Salary (descending).

16. Reset the index after sorting.

17. Print the top 3 employees with the highest Salary.

18. Print the last 2 employees after sorting by Age.

19. Count how many employees earn more than the average Salary.

20. Print all unique City names in alphabetical order.
"""
import pandas as pd

data = {
    "Name": ["Kiran", "Rahul", "Anjali", "Priya", "Vikram", "Sneha", "Arjun", "Pooja", "Rohit", "Neha"],
    "Age": [18, 22, 21, 19, 25, 23, 20, 24, 27, 26],
    "City": ["Hassan", "Mysore", "Hassan", "Bangalore", "Mysore",
             "Hassan", "Bangalore", "Hassan", "Mysore", "Bangalore"],
    "Salary": [25000, 40000, 35000, 28000, 50000,
               42000, 30000, 45000, 55000, 48000]
}

df = pd.DataFrame(data)
print(df["Salary"]>40000)
print((df["Age"]>20) & (df["Age"]<25))
print(df[df["City"] == "Hassan"][["Name", "Salary"]])
print(df["Salary"].sort_values(ascending=False).iloc[1])
print(df["Salary"].sort_values(ascending=False).iloc[2])
print(df[df["Salary"] == df["Salary"].max()][["Name", "Salary"]])
print(df[df["Salary"] == df["Salary"].min()][["Name","Salary"]])
print(df.groupby("City")["Name"].count())
print(df.groupby("City")["Age"].mean())
print(df.groupby("City")["Salary"].sum())
df["Experience"]=1
print(df["Experience"])
df["Salary"] = df["Salary"]*0.05
print(df["Salary"])
df["Monthly-Tax"] = df["Salary"]*0.08
print(df["Monthly-Tax"])
print(df)
df.drop(columns=["Experience"], inplace=True)
print(df)
print(df[["Name","Salary"]].sort_values(["Name","Salary"],ascending=[True,False]))
df.reset_index
print(df)
print(df[["Name","Age"]].sort_values(["Age"],ascending=True))
print((df["Salary"] > df["Salary"].mean()).sum())
print((df["City"].sort_values(ascending=True)).unique())