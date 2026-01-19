#slicing pandas dataframe using iloc[]

import pandas as pd

#creating a custom dataframe

player_list = [['M.S.Dhoni', 36, 75, 5428000],
               ['A.B.D Villers', 38, 74, 3428000],
               ['V.Kohli', 31, 70, 8428000],
               ['S.Smith', 34, 80, 4428000],
               ['C.Gayle', 40, 100, 4528000],
               ['J.Root', 33, 72, 7028000],
               ['K.Peterson', 42, 85, 2528000]]

df = pd.DataFrame(player_list, columns = ["Name", "Age", "Weight", "Salary"])

print("Dataset: ")
print(df)

#slicing rows in dataframe
df1 = df.iloc[0:5]
print("Slicing rows in dataframe ")
print(df1)

#slicing columns in dataframe
df2 = df.iloc[:, 0:2]
print("Slicing columns in dataframe ")
print(df2)

#slicing specific cell
df3 = df.iloc[2, 3]
print("Specific cell Value: ", df3)

#using boolean conditions in a pandas dataframe
data = df[df['Age'] > 35].iloc[:, :]
print("\nFiltered Data based on age > 35\n", data)

#slicing using loc
#similar to iloc but should use name instead
