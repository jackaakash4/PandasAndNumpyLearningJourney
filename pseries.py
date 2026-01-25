#creating an empty pandas series

import pandas as pd
import numpy as np

ser = pd.Series()
print("\nEmpty series")
print(ser)

#creating a series from a numpy array
data = np.array([1, 2, 3, 4, 5])
print("\nSeries from a numpy array")

series = pd.Series(data)
print(series)


#creating a series from a list
data_list = ['A', 'a', 'k' ,'a', 's', 'h']
print("\nSeries from a list")
list_series = pd.Series(data_list)
print(list_series)
