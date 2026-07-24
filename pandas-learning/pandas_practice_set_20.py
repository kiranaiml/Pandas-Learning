"""
Print the DataFrame.
Set "Name" as the index.
Convert the DataFrame into a stacked Series using stack().
Print the stacked object.
Print the type of the stacked object.
Print the shape of the stacked object.
Count the total number of values in the stacked object.
Print only Kiran's marks from the stacked object.
Print only Rahul's English mark from the stacked object.
Print all Science marks from the stacked object.
Find the highest mark using the stacked object.
Find the lowest mark using the stacked object.
Find the average of all marks using the stacked object.
Sort the stacked values in ascending order.
Sort the stacked values in descending order.
Convert the stacked object back into a DataFrame using unstack().
Check whether the unstacked DataFrame is equal to the original indexed DataFrame.
Reset the index of the stacked object.
Rename the columns to "Name", "Subject", and "Marks".
Save the final DataFrame to a CSV file named stack_unstack_output.csv.
"""
import pandas as pd

data = {
    "Name": ["Kiran", "Rahul", "Anjali"],
    "Math": [90, 85, 88],
    "Science": [95, 80, 92],
    "English": [85, 90, 87]
}

df = pd.DataFrame(data)

print(df)
print(df.melt(id_vars="Name"))
print(df.stack())
print(df.stack().shape)
print(df.stack("Kiran"))