#Arithmatic operations on data frame
import pandas as pd

df1 = pd.DataFrame({
    'A': [10, 20, 30],
    'B': [40, 50, 60]})

df2 = pd.DataFrame({
    'A': [1, 2, 3], 
    'B': [4, 5, 6]
    })

#subtracting the dataframes
result = df1 - df2
print("Dataframe: \n", df1, "\n", df2, "\n")
print("Subtraction of dataframe: \n", result)


#comparision operations on data frame
comp = df1 > df2
print("\nComparision between dataframe\n", comp)
