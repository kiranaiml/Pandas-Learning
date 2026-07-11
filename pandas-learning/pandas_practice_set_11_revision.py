"""
Pandas Practice Set 11 - Duplicate Data (Revision)

1. Print the DataFrame.

2. Check whether duplicate rows exist.

3. Count the total duplicate rows.

4. Print only duplicate rows.

5. Print only non-duplicate rows.

6. Remove duplicate rows.

7. Print the DataFrame after removing duplicates.

8. Print the shape before removing duplicates.

9. Print the shape after removing duplicates.

10. Reset the index after removing duplicates.

11. Check whether duplicate rows still exist.

12. Print only the Name column after removing duplicates.

13. Print the employee with the highest Salary after removing duplicates.

14. Sort the cleaned DataFrame by Salary (highest to lowest).

15. Count employees in each City after removing duplicates.

16. Find how many unique cities are present.

17. Print all unique city names.

18. Add a Bonus column = 10% of Salary.

19. Save the cleaned DataFrame as "employees_clean_duplicates.csv" without the index.

20. Read "employees_clean_duplicates.csv" and print it.
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
print(df.duplicated().count())
print(df[df.duplicated()])
print(df.drop_duplicates())
print(df.drop_duplicates())
print(pd.DataFrame(data))
print(pd.DataFrame(data).shape)
print(df.shape)
print(df.reset_index())
print(df.duplicated())
print(df["Name"])
print(df[df["Salary"]==df["Salary"].max()])
print(df["Salary"].sort_values(ascending=False))
print(df.groupby("City")["Name"].count())
print(df["City"].nunique())
print(df["City"].unique())
df["Bonus"]=df["Salary"]*0.10
print(df.drop_duplicates(inplace=True))
df.to_csv("employees_clean_duplicate.csv")
print(pd.read_csv("employees_clean_duplicate.csv"))