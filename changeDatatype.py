#changeing datatypes 

import pandas as pd

data = {'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'], 
        'Age': [25, 30, 22, 35, 28], 
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'], 
        'Salary': [50000, 55000, 40000, 70000, 48000]}

df = pd.DataFrame(data)
print("The datatypes of Age field before change is: ", df['Age'].dtypes)
df['Age'] = df['Age'].astype(float)
print("The datatypes of Age field after change is : ", df['Age'].dtypes)

#converting a column to a DateTime type
df['Join Date'] = ['2021-01-01', '2020-05-22', '2022-03-15', '2021-07-30', '2020-11-11']
print(df)

df['Join Date'] = pd.to_datetime(df['Join Date'])
print("Datatype of Join Date column is ", df['Join Date'].dtypes)

#changing multiple columns' Data Types
df = df.astype({'Age': 'float64', 'Salary': 'str'})
print("\nAfter changing multiple columns' Datatypes ",df.dtypes)
