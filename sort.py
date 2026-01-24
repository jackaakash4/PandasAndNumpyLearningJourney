#sorting Dataframe by a single column using sort_values()

import pandas as pd

data = {
        'Name': ['Aakash', 'Shrestha', 'Jack'],
        'Age': [23, 16, 23]
        }

df1 = pd.DataFrame(data)

sorted_df = df1.sort_values( by = 'Age', ascending = False, ignore_index = True)
print(sorted_df)
