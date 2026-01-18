#indexing data using the [] operator

import pandas as pd

data = pd.read_csv("people_data.csv", index_col = "Email")
print("Dataset: ")
print(data.head(5))


#selecting a single column
first = data["First Name"]
print("\nSingle column selected from dataset")
print(first.head(5))

#selecting multiple columns

columns = data[["First Name", "Last Name"]]
print("\nSelected multiple columns from dataset")
print(columns.head(5))
