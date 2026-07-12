"""

Pandas Practice Set 16 - Map

1. Print the DataFrame.

2. Create a new column DepartmentCode using map():
   IT → 101
   HR → 102
   Finance → 103

3. Create a new column TaxRate using map():
   IT → 10%
   HR → 8%
   Finance → 5%

4. Calculate TaxAmount = Salary × TaxRate.

5. Print Name, Department, DepartmentCode and TaxAmount.

6. Print employees whose DepartmentCode is 101.

7. Find the average Salary for each Department.

8. Sort by Salary (highest to lowest).

9. Save as "map_data.csv" without the index.

10. Read the CSV and print it.
"""
import pandas as pd

data = {
    "Name": ["Kiran", "Rahul", "Anjali", "Priya", "Vikram"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [25000, 40000, 35000, 28000, 50000]
}

df = pd.DataFrame(data)
print(df)

df["DepartmentCode"] = df["Department"].map({
    "IT": 101,
    "HR": 102,
    "Finance": 103
})

df["TaxRate"] = df["Department"].map({
    "IT": 10,
    "HR": 8,
    "Finance": 5
})

df["TaxAmount"] = df["Salary"] * df["TaxRate"] /100
print(df["TaxAmount"])
print(df)
print(df[df["DepartmentCode"]==101]["Name"])
print(df.groupby("Department")["Salary"].mean())
df.sort_values(by="Salary",ascending=False,inplace=True)
print(df)
df.to_csv("map_data.csv",index=False)
print(pd.read_csv("map_data.csv"))