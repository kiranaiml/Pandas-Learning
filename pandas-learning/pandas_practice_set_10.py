
"""
Pandas Practice Set - 10 (Missing Values)

1. Print the DataFrame.

2. Print the first 5 rows.

3. Print the last 3 rows.

4. Find how many missing values are present in each column.

5. Find the total number of missing values in the DataFrame.

6. Print only the rows that contain at least one missing value.

7. Remove all rows that contain missing values.

8. Replace missing Salary values with 0.

9. Replace missing Age values with the average Age.

10. Replace missing City values with "Unknown".

11. Check whether there are any missing values left.

12. Print the average Salary (after filling missing values).

13. Print the maximum Age.

14. Print all employees whose Salary is greater than 40000.

15. Count employees city-wise.

16. Add a new column named Bonus = 10% of Salary.

17. Remove rows where Salary is 0.

18. Reset the index.

19. Save the cleaned DataFrame as "employees_clean.csv".

20. Read "employees_clean.csv" and print it.
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
print(df.head(5))
print(df.tail(3))

print(df.isna().sum())
print(df.isna().sum().sum())

print(df[df.isna().any(axis=1)])

df_dropped = df.dropna()
print(df_dropped)

df["Salary"] = df["Salary"].fillna(0)
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["City"] = df["City"].fillna("Unknown")

print(df.isna().sum())

print(df["Salary"].mean())
print(df["Age"].max())

print(df[df["Salary"] > 40000])

print(df.groupby("City")["Name"].count())

df["Bonus"] = df["Salary"] * 0.10

df = df[df["Salary"] != 0]

df.reset_index(drop=True, inplace=True)

df.to_csv("employees_clean.csv", index=False)

clean_df = pd.read_csv("employees_clean.csv")
print(clean_df)