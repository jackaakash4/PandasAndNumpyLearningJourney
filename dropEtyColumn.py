#dropping empty columns in pandas
#dropna() function

import pandas as pd
import numpy as np

df = pd.DataFrame({
        "FirstName": ["Aakash", "Aryan", "Abishek"],
        "Gender": ["", "", ""],
        "Age": [0, 0, 0]
        })

df['Department'] = np.nan
print(df)

#remove all null values column
df.dropna(how = 'all', axis = 1, inplace = True)
#inplace = True means apply in the same dataframe rather than returning new dataframe 
#how = 'all' means remove column where all values are nan
#axis = 1 means column. And axis = 0 means index or row

print("\nAfter removing columns with all empty values\n", df)

