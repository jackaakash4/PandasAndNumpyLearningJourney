#merging dataframe using the how argument

import pandas as pd

data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1': ['K0', 'K1', 'K0', 'K1'],
         'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],}

data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1': ['K0', 'K0', 'K0', 'K0'],
         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']}

#display the dataframe

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print("Dataframes: \n\n", df1, "\n\n", df2)


#merging with how argument: how = inner, outer, left, right

inner = pd.merge(df1, df2, how = 'inner', on = ['key', 'key1'])
print("Inner merge \n")
print(inner)


#Outer join
outer = pd.merge(df1, df2, how = 'outer', on = ['key', 'key1'])
print("Outer merge \n")
print(outer)

#outer left join
left = pd.merge(df1, df2, how = 'left', on = ['key', 'key1'])
print("Outer left merge \n")
print(left)

#outer right join
right = pd.merge(df1, df2, how = 'right', on = ['key', 'key1'])
print("Outer right merge \n")
print(right)

