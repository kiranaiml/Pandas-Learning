"""
Pandas Practice Set 12 - Merge DataFrames

1. Print both DataFrames.

2. Merge both DataFrames using EmpID.

3. Print the merged DataFrame.

4. Print only Name and Salary.

5. Print the employee with the highest Salary.

6. Print employees whose Salary is greater than 50000.

7. Count employees in each Department.

8. Sort the merged DataFrame by Salary (highest to lowest).

9. Add a Bonus column = 10% of Salary.

10. Add a Tax column = 5% of Salary.

11. Add a NetSalary column = Salary + Bonus - Tax.

12. Print only Name and NetSalary.

13. Print the average Salary.

14. Print the maximum Salary.

15. Print the minimum Salary.

16. Print all column names.

17. Print the DataFrame shape.

18. Save the merged DataFrame as "employee_salary.csv" without the index.

19. Read "employee_salary.csv" and print it.

20. Print DataFrame information using info().
"""
import pandas as pd

employees = {
    "EmpID": [101, 102, 103, 104],
    "Name": ["Kiran", "Rahul", "Anjali", "Priya"],
    "Department": ["IT", "HR", "Finance", "IT"]
}

df_emp = pd.DataFrame(employees)

print(df_emp)
salary = {
    "EmpID": [101, 102, 103, 105],
    "Salary": [50000, 45000, 60000, 70000]
}

df_salary = pd.DataFrame(salary)

print(df_salary)

data=pd.merge(df_emp,df_salary,on="EmpID")
print(data[["Name","Salary"]])
print(data[data["Salary"]>50000]["Name"])
#print(data[data["Salary"]==data["Salary"].max()])
print(data.groupby("Department")["Name"].count())
print(data.sort_values(by="Salary",ascending=False))
data["Bonus"]= data["Salary"]*0.10
print(data)
data["tax"]=data["Salary"]*0.05
print(data)
data["NetSalary"]=data["Salary"]+data["Bonus"]-data["tax"]
print(data)
print(data[["Name","NetSalary"]])
print(data["Salary"].mean())
print(data["Salary"].max())
print(data["Salary"].min())
print(data.shape)
print(data.columns)
data.to_csv("employees_Salary.csv",index=False)
print(pd.read_csv("employees_Salary.csv"))
print(data.info())