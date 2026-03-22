#string manipulation in pandas

import pandas as pd
import numpy as np

data = { 'Name': ['Lukas', 'Sofia', 'Hiroshi', 'Marta', 'Yannis', np.nan, 'Elena'],
         'City': ['Berlin', 'Madrid', 'Tokyo', 'Warsaw', 'Athens', 'Oslo', 'Lisbon'] }

#cat() method to concat all string in the column into a single string using a chosen separator

df = pd.DataFrame(data)

print("Concat: \n", df['Name'].str.cat(sep=' '))
