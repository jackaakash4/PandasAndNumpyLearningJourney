#using interpolate() function fills missing values using interpolation techniques such as the linear method

import pandas as pd

df = pd.DataFrame({"A": [12, 4, 5, None, 1], 
                   "B": [None, 2, 54, 3, None], 
                   "C": [20, 16, None, 3, 8], 
                   "D": [14, 3, None, None, 6]}) 
print(df)

print("\nAfter interpolate")
print(df.interpolate(method = "linear", limit_direction = "forward"))

