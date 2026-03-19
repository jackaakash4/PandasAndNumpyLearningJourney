#remove duplicate rows from a dataframe based on all columns or specific one using drop_duplicate()

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Alice", "David"],
    "Age": [25, 30, 25, 40],
    "City": ["NY", "LA", "NY", "Chicago"]
}

df = pd.DataFrame(data)

print("Original DataFrame: ", df)

#after removing the duplicates row

df_nodup = df.drop_duplicates()

print("\nAfter removing duplicates from dataframe: ", df_nodup)

        
