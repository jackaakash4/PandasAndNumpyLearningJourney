#indexing with .iloc[]
#similar to iloc[] but accept only integer

import pandas as pd
data = pd.read_csv("people_data.csv", index_col = "First Name")

#selecting a single row by position
print("\nSelecting a single row by position")
row = data.iloc[1]
print(row)

#selecting mulitple rows by position
print("\nSelecting multiple rows by position")
rows = data.iloc[[1, 2, 3]]
print(rows)

#selecting specific rows and columns
print("\nSelecting specific rows and columns")
selection = data.iloc[[0, 1], [1, 2, 3]]
print(selection)

#selecting all rows and specific columns by position
print("\nSelecting all rows and specific columns by position")
allSelection = data.iloc[:, [0, 1]]
print(allSelection)

