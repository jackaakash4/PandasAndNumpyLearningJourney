#remove duplicate rows from a dataframe based on all columns or specific one using drop_duplicate()

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Alice", "David"],
    "Age": [25, 30, 25, 40],
    "City": ["NY", "LA", "NY", "Chicago"]
}

df = pd.DataFrame(data)

print("Original DataFrame: \n", df)

#after removing the duplicates row

df_nodup = df.drop_duplicates()

print("\nAfter removing duplicates from dataframe:\n", df_nodup)

#dropping based on specific column
df_cleaned = df.drop_duplicates(subset= ["City"])
print("\nAfter removing duplicates from city column \n", df_cleaned)

#keeping the last occurance of duplicates
df_last = df.drop_duplicates(keep="last")
print("\nKeepin=g the last occurance of duplicates \n", df_last)

#dropping all duplicates
df_all = df.drop_duplicates(keep = False)
print("\nAfter dropping all duplicates \n", df_all)

#modifying the original dataframe directily
df.drop_duplicates(inplace = True)
print("Modifying the original dataframe directly\n", df) 

