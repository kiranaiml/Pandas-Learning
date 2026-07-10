"""
Pandas Practice Set 11 - Duplicate Data

1. Print the DataFrame.

2. Check whether there are duplicate rows.

3. Count the total number of duplicate rows.

4. Print only the duplicate rows.

5. Remove duplicate rows.

6. Print the DataFrame after removing duplicates.

7. Print the shape before removing duplicates.

8. Print the shape after removing duplicates.

9. Remove duplicates and reset the index.

10. Check whether duplicate rows still exist.

11. Print only the Name column after removing duplicates.

12. Find how many unique cities are present.

13. Print all unique city names.

14. Count employees in each city after removing duplicates.

15. Print the employee with the highest salary after removing duplicates.

16. Sort the cleaned DataFrame by Salary (highest to lowest).

17. Add a new column named Bonus = 10% of Salary.

18. Save the cleaned DataFrame as "employees_duplicates_removed.csv" without the index.

19. Read "employees_duplicates_removed.csv" and print it.

20. Print the final DataFrame information using info().
"""
import pandas as pd

data = {
    "Name": [
        "Kiran", "Rahul", "Anjali", "Priya", "Vikram",
        "Sneha", "Arjun", "Pooja", "Rahul", "Sneha",
        "Neha", "Kiran"
    ],
    "Age": [
        18, 22, 21, 19, 25,
        23, 20, 24, 22, 23,
        26, 18
    ],
    "City": [
        "Hassan", "Mysore", "Hassan", "Bangalore", "Mysore",
        "Hassan", "Bangalore", "Hassan", "Mysore", "Hassan",
        "Bangalore", "Hassan"
    ],
    "Salary": [
        25000, 40000, 35000, 28000, 50000,
        42000, 30000, 45000, 40000, 42000,
        48000, 25000
    ]
}

df = pd.DataFrame(data)

print(df)

print(df.duplicated())

print(df.duplicated().sum())

print(df[df.duplicated()])

df = df.drop_duplicates()

print(df)

print(pd.DataFrame(data).shape)

print(df.shape)

df.reset_index(drop=True, inplace=True)
print(df)

print(df.duplicated().sum())

print(df["Name"])

print(df["City"].nunique())

print(df["City"].unique())

print(df.groupby("City")["Name"].count())

print(df[df["Salary"] == df["Salary"].max()])

print(df.sort_values(by="Salary", ascending=False))

df["Bonus"] = df["Salary"] * 0.10
print(df)
df.to_csv("employees_duplicates_removed.csv", index=False)

new_df = pd.read_csv("employees_duplicates_removed.csv")
print(new_df)

df.info()