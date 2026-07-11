"""
Pandas Practice Set 11 - Final (Duplicate Data)

1. Print the DataFrame.

2. Check whether duplicate rows exist.

3. Count the total duplicate rows.

4. Print only duplicate rows.

5. Print only non-duplicate rows.

6. Remove duplicate rows.

7. Print the DataFrame after removing duplicates.

8. Print the shape before removing duplicates.

9. Reset the index after removing duplicates.

10. Check whether duplicate rows still exist.

11. Print only the Name and Salary columns.

12. Print the employee with the highest Salary.

13. Print employees whose Salary is greater than 40000.

14. Count employees in each City.

15. Print all unique city names.

16. Print the total number of unique cities.

17. Add a Bonus column = 10% of Salary.

18. Sort the DataFrame by Salary (highest to lowest).

19. Save the cleaned DataFrame as "employees_final.csv" without the index.

20. Read "employees_final.csv" and print it.
"""
import pandas as pd

data = {
    "ID": [1, 2, 3, 4, 5, 3, 2, 6, 7, 8, 8],
    "Name": [
        "Kiran", "Rahul", "Anjali", "Priya", "Vikram",
        "Anjali", "Rahul", "Sneha", "Neha", "Arjun", "Arjun"
    ],
    "Age": [18, 22, 21, 19, 25, 21, 22, 23, 26, 20, 20],
    "City": [
        "Hassan", "Mysore", "Hassan", "Bangalore", "Mysore",
        "Hassan", "Mysore", "Hassan", "Bangalore", "Bangalore", "Bangalore"
    ],
    "Salary": [
        25000, 40000, 35000, 28000, 50000,
        35000, 40000, 42000, 48000, 30000, 30000
    ]
}

df = pd.DataFrame(data)

print(df)
print(df.duplicated())
print(df.duplicated().sum())
print(df.drop_duplicates(inplace=True))
print(df)
print(pd.DataFrame(data).shape)
print(df.shape)
df.reset_index(drop=True,inplace=True)
print(df.duplicated())
print(df[["Name","Salary"]])
print(df[df["Salary"]== df["Salary"].max()])
print(df[df["Salary"]>40000]["Name"])
print(df.groupby("City")["Name"].count())
print(df["City"].unique())
print(df["City"].unique())
df["Bonus"]=df["Salary"]*0.10
print(df.sort_values(by="Salary",inplace=True))
df.to_csv("employees_final.csv",index=False)
print(pd.read_csv("employees_final.csv"))