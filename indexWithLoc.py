#selecting a single row by label

import pandas as pd

data = pd.read_csv("People_data.csv", index_col = "First Name")
print("Dataset: ")
print(data.head(5))

#selecting a single row by label
print("\nSelecting a single row by label")
row = data.loc["Lori"]
print(row.head(5))

#selecting muktiple rows by label
print("\nSelecting multiple rows by label")
rows = data.loc[["Lori", "Shelby"]]
print(rows.head(5))

#selecting specific rows and columns
print("\nSelecting specific rows and columns")
selection = data.loc[["Lori", "Shelby"], ["Last Name", "Email"]]
print(selection.head(5))

#selecting all rows and specific columns
print("\nSelecting all rows and specific columns")
specific_selection = data.loc[:, ["Last Name", "Email"]]
print(specific_selection)

