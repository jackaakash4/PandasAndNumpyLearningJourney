import pandas as pd
import numpy as np

s = pd.Series()
print("Pandas Series: ", s)

data = np.array(['J', 'A', 'C', 'K'])

s = pd.Series(data)
print("Pandas Series: \n", s)

