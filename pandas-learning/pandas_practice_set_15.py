"""
Pandas Practice Set 15 - Apply

1. Print the DataFrame.

2. Create a new column Tax = 5% of Salary using apply().

3. Create a new column Bonus = 10% of Salary using apply().

4. Create a new column NetSalary = Salary + Bonus - Tax.

5. Convert all names to uppercase using apply().

6. Convert all names to lowercase using apply().

7. Print employees whose NetSalary is greater than 50000.

8. Print the average NetSalary.

9. Sort by NetSalary (highest to lowest).

10. Save as "apply_data.csv" without the index.

11. Read the CSV and print it.

12. Print DataFrame information using info().
"""
import pandas as pd

data = {
    "Name": ["Kiran", "Rahul", "Anjali", "Priya", "Vikram"],
    "Salary": [25000, 40000, 35000, 28000, 50000]
}

df = pd.DataFrame(data)

print(df)
df["Tax"] = df["Salary"].apply(lambda x: x * 0.05)
df["Bonus"] = df["Salary"].apply(lambda x : x*0.10)
df["NetSalary"] = df["Bonus"]+df["Salary"]-df["Tax"]
print(df)
df["Name"] = df["Name"].str.upper()
print(df)
df["Name"] = df["Name"].str.lower()
print(df)
print(df[df["Salary"] == df["Salary"].max()])
print(df["NetSalary"].mean())
df.sort_values(by="NetSalary",ascending=False,inplace=True)
print(df["NetSalary"])
df.to_csv("apply_data.csv",index=False)
print(pd.read_csv("apply_data.csv"))
df.info()