import pandas as pd

#read the excel file 
df = pd.read_excel('students.xlsx', sheet_name = 0, index_col = 0)
print(df)

#loading multiple sheets using concat()
file = 'students.xlsx'

sheet1 = pd.read_excel(file,
                       sheet_name = 0,
                       index_col = 0
                       )

sheet2 = pd.read_excel(file,
                       sheet_name = 1,
                       index_col = 0
                       )

newData = pd.concat([sheet1, sheet2])
print(newData)
