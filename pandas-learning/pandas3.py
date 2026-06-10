import pandas as pd
data={
    "Name":["Kiran", "Rahul", "Priya", "Amit", "Sneha", "Ravi", "Anjali", "Vijay", "Pooja", "Arjun"],
    "Age":[18, 21, 20, 22, 19, 23, 21, 24, 20, 22],
    "City":["Hassan", "Bengaluru", "Mysuru", "Mangaluru", "Hubballi", "Belagavi", "Shivamogga", "Davanagere", "Tumakuru", "Udupi"]

}
df=pd.DataFrame(data)
print(df)
df.to_csv('data.csv')
df.to_excel('data1.xlsx')
df.to_json('data2.json')