"""
Pandas Practice Set 13 - Merge Joins

1. Print both DataFrames.

2. Perform an Inner Join.

3. Perform a Left Join.

4. Perform a Right Join.

5. Perform an Outer Join.

6. Print the shape of every join.

7. Find which employee has no Salary.

8. Find which Salary record has no employee.

9. Replace missing Salary with 0.

10. Sort the final DataFrame by Salary (highest to lowest).

11. Add Bonus = 10% of Salary.

12. Add Tax = 5% of Salary.

13. Add NetSalary = Salary + Bonus - Tax.

14. Save as "employee_join.csv" without index.

15. Read the CSV and print it.
"""
import pandas as pd

employees = {
    "EmpID": [101, 102, 103, 104],
    "Name": ["Kiran", "Rahul", "Anjali", "Priya"]
}

salary = {
    "EmpID": [101, 102, 103, 105],
    "Salary": [50000, 45000, 60000, 70000]
}

df_emp = pd.DataFrame(employees)
df_salary = pd.DataFrame(salary)
data=pd.merge(df_emp,df_salary,on="EmpID",how="inner")
print(data)
data1=pd.merge(df_emp,df_salary,on="EmpID",how="left")
print(data1)
data2=pd.merge(df_emp,df_salary,on="EmpID",how="right")
print(data2)
data3=pd.merge(df_emp,df_salary,on="EmpID",how="outer")
print(data3)
print(data.shape)
print(data1.shape)
print(data2.shape)
print(data3.shape)
print(data[data["Salary"].isna()]["Name"])
print(data1[data1["Salary"].isna()]["Name"])
print(data2[data2["Salary"].isna()]["Name"])
print(data3[data3["Salary"].isna()]["Name"])
print(data[data["Name"].isna()]["EmpID"])
print(data1[data1["Name"].isna()]["EmpID"])
print(data2[data2["Name"].isna()]["EmpID"])
print(data3[data3["Name"].isna()]["EmpID"])
data3["Salary"] = data3["Salary"].fillna(0)
print(data3)
print(data.sort_values(by="Salary",ascending=False))
print(data1.sort_values(by="Salary",ascending=False))
print(data2.sort_values(by="Salary",ascending=False))
print(data3.sort_values(by="Salary",ascending=False))
data["Bonus"]=data["Salary"]*0.10
data1["Bonus"]=data1["Salary"]*0.10
data2["Bonus"]=data2["Salary"]*0.10
data3["Bonus"]=data3["Salary"]*0.10
data["tax"]=data["Salary"]*0.05
data1["tax"]=data1["Salary"]*0.05
data2["tax"]=data2["Salary"]*0.05
data3["tax"]=data3["Salary"]*0.05
data["NetSalary"]=data["Salary"]+data["Bonus"]-data["tax"]
data1["NetSalary"]=data1["Salary"]+data1["Bonus"]-data1["tax"]
data2["NetSalary"]=data2["Salary"]+data2["Bonus"]-data2["tax"]
data3["NetSalary"]=data3["Salary"]+data3["Bonus"]-data3["tax"]
data.to_csv("employees_join.csv")
data1.to_csv("employees_join1.csv")
data2.to_csv("employees_join2.csv")
data3.to_csv("employees_join3.csv")
print(pd.read_csv("employees_join.csv"))
print(pd.read_csv("employees_join1.csv"))
print(pd.read_csv("employees_join2.csv"))
print(pd.read_csv("employees_join3.csv"))