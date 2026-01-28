import pandas as pd

s1 = pd.Series([True, False, True, False])
s2 = pd.Series([True, True, False, False])

print("Series s1: \n", s1, "\nSeries s2 \n", s2)


#applying logical and
result = s1 & s2
print("Logical And: \n", result)

#handling missing data in binary operaions


df1 = pd.DataFrame({
        'A': [1, 2, None], 'B': [4, None, 5]
        })

df2 = pd.DataFrame({
        'A': [1, None, 3], 'B': [None, 5, 6]
        })

print("\nDataframes df1: \n", df1, "\nDataFrame df2\n", df2)

add = df1 + df2
print("\nAdding two dataframe", add)

