#using replace() function to replace NaN values with a specific value.

import numpy as np
import pandas as pd

data = pd.read_csv("employees.csv")

print(data[15:25])


replaced_data = data.replace(to_replace = np.nan, value = -99)
print(replaced_data[15:25])
