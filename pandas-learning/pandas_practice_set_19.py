"""
=========================
PANDAS PRACTICE SET 9
Topic: melt()
=========================



-------------------------------------------------
LEVEL 1
-------------------------------------------------

1. Melt the DataFrame by keeping Name as the identifier.

2. Rename:
   variable → Subject
   value → Marks

3. Melt only the Math and Science columns.

4. Melt only the English column.

5. Keep Name as id_vars and rename:
   variable → Exam
   value → Score

-------------------------------------------------
LEVEL 2
-------------------------------------------------

6. Create a new DataFrame after melting and print it.

7. Print only the Subject column from the melted DataFrame.

8. Print only the Marks column from the melted DataFrame.

9. Print all rows where Marks are greater than 90.

10. Sort the melted DataFrame by Marks in descending order.

-------------------------------------------------
LEVEL 3
-------------------------------------------------

11. Find the highest mark after melting.

12. Find the average mark after melting.

13. Count how many records are present after melting.

14. Print all rows where Subject is "Math".

15. Print all rows where Subject is "Science".

16. Print all rows where Subject is "English".

17. Find the maximum mark for each Subject using groupby().

18. Find the average mark for each Subject.

19. Find the minimum mark for each Subject.

20. Find the total marks for each Subject.
"""
import pandas as pd

data = {
    "Name": ["Kiran", "Rahul", "Anjali", "Priya"],
    "Math": [90, 80, 85, 95],
    "Science": [88, 91, 84, 89],
    "English": [92, 86, 87, 90]
}

df = pd.DataFrame(data)

print(df)
print(df.melt(id_vars="Name"))
print(df.melt(id_vars="Name",var_name="Subject",value_name="Mark"))
print(df.melt(id_vars="Name",value_vars=["Math","Science"]))
print(df.melt(id_vars="Name",value_vars="English",value_name="Mark",var_name="Subject"))
print(df.melt(id_vars="Name",value_name="Score",var_name="Exam"))

"""
Level 2
"""
df1=pd.DataFrame(data)
df1.melt(var_name="Subject")
print(df1["Subject"])