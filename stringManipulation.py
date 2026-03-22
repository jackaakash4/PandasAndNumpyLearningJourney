#string manipulation in pandas

import pandas as pd
import numpy as np

data = { 'Name': ['Lukas', 'Sofia', 'Hiroshi', 'Marta', 'Yannis', np.nan, 'Elena'],
         'City': ['Berlin', 'Madrid', 'Tokyo', 'Warsaw', 'Athens', 'Oslo', 'Lisbon'] }

#cat() method to concat all string in the column into a single string using a chosen separator

df = pd.DataFrame(data)

print("Concat: \n", df['Name'].str.cat(sep=' '))

#get_dummies() method converts each unique string into a separate one-hot encoded column for modeling
print("Converted each unique string into a separate encoded column\n", df['City'].str.get_dummies())

#startswith() to check whether each string begins with the specific prefix

print("Checking: \n", df['Name'].str.startswith('M'))

