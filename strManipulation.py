#string manipulations in pandas dataframe

import pandas as pd
import numpy as np

data = { 'Name': ['Lukas', 'Sofia', 'Hiroshi', 'Marta', 'Yannis', np.nan, 'Elena'],
         'City': ['Berlin', 'Madrid', 'Tokyo', 'Warsaw', 'Athens', 'Oslo', 'Lisbon'] }

df = pd.DataFrame(data)
print("Dataframe: \n", df)

