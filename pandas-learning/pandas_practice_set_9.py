"""
Pandas Practice Set - Level 9

1. Print employees whose Salary is between 30000 and 50000.

2. Print employees who are from Hassan and Age is greater than 20.

3. Print Name, City and Salary of employees whose Salary is greater than the average Salary.

4. Find the average Salary of employees from Hassan only.

5. Find the highest Salary in each City.

6. Find the employee(s) whose Salary is exactly 45000.

7. Add a new column named YearlySalary (Salary × 12).

8. Add a new column named Bonus equal to 10% of Salary.

9. Create a new column named NetSalary = Salary + Bonus.

10. Print only Name, Salary, Bonus and NetSalary.

11. Remove the Bonus column.

12. Rename the column "City" to "Location".

13. Print all column names.

14. Print the number of rows and columns.

15. Sort the DataFrame by Age (descending).

16. Print the first employee after sorting by Salary (highest first).

17. Print the last employee after sorting by Age (ascending).

18. Count how many employees belong to Hassan.

19. Print the employee(s) whose Age is equal to the maximum Age.

20. Save the DataFrame as "employees.csv".
"""
import pandas as pd

data = {
    "Name": ["Kiran", "Rahul", "Anjali", "Priya", "Vikram", "Sneha", "Arjun", "Pooja", "Rohit", "Neha"],
    "Age": [18, 22, 21, 19, 25, 23, 20, 24, 27, 26],
    "City": [
        "Hassan", "Mysore", "Hassan", "Bangalore", "Mysore",
        "Hassan", "Bangalore", "Hassan", "Mysore", "Bangalore"
    ],
    "Salary": [25000, 40000, 35000, 28000, 50000, 42000, 30000, 45000, 55000, 48000]
}

df = pd.DataFrame(data)

print(df)
print((df["Salary"]>30000) & (df["Salary"]<50000))
print((df["City"]=="Hassan")&(df["Age"]>20))
print(df[df["Salary"] > df["Salary"].mean()][["Name","City","Salary"]])
print(df[df["City"]=="Hassan"][["Salary"]].mean())
print(df.groupby("City")["Salary"].max())
print(df[df["Salary"]==45000]["Name"])
df["Yearly Salary"]=df["Salary"]*12
df["Bonus"]=df["Salary"]*0.10
df["Net Salary"]=df["Salary"]+df["Bonus"]
print(df[["Name","Salary","Net Salary","Bonus"]])
df.drop(columns=["Bonus"], inplace=True)
df.rename(columns={"City":"Location"},inplace=True)
print(df)
print(df.columns)
print(df.shape)
print(df["Age"].sort_values(ascending=False))
print(df[df["Salary"] == df["Salary"].max()]["Name"])
print(df.sort_values(by="Age", ascending=True).tail(1))
print(df[df["Age"] == df["Age"].max()]["Name"])
df.to_csv("employees.csv", index=False)