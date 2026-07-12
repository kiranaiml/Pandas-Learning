"""
Pandas Practice Set 17 - Replace

1. Print the DataFrame.

2. Replace "IT" with "Information Technology".

3. Replace "HR" with "Human Resources".

4. Replace "Finance" with "Accounts".

5. Replace Salary 25000 with 26000.

6. Replace Salary 50000 with 55000.

7. Print employees whose Department is "Human Resources".

8. Print the maximum Salary.

9. Add Bonus = 10% of Salary.

10. Add NetSalary = Salary + Bonus.

11. Sort by NetSalary (highest to lowest).

12. Save as "replace_data.csv" without the index.

13. Read the CSV and print it.

14. Print the DataFrame shape.

15. Print all column names."""
import pandas as pd

data = {
    "Name": ["Kiran", "Rahul", "Anjali", "Priya", "Vikram"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [25000, 40000, 35000, 28000, 50000]
}

df = pd.DataFrame(data)

print(df)
df["Department"]=df["Department"].replace({
    "IT":"Information Technology",
    "HR":"Human Resource",
    "Finance":"Accounts"
})
print(df["Department"])
df["Salary"]=df["Salary"].replace({
    25000:26000,
    50000:55000
})
print(df["Salary"])
print(df[df["Department"]=="Human Resource"]["Name"])
print(df["Salary"].max())
df["Bonus"]=df["Salary"]*0.10
print(df["Bonus"])
df["NetSalary"]=df["Salary"]+df["Bonus"]
print(df["NetSalary"])
df.sort_values(by="NetSalary",ascending=False,inplace=True)
df.to_csv("replace_data.csv",index=False)
print(pd.read_csv("replace_data.csv"))
print(df.shape)
print(df.columns)