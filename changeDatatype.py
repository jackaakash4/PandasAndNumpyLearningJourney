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
