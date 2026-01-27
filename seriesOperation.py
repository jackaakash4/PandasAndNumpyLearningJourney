#Binary operations on series

import pandas as pd

s1 = pd.Series([10, 9, 8], index = ['a', 'b', 'c'])
s2 = pd.Series([1, 2 ,3], index = ['a', 'b', 'c'])
#printing the series
print("Series: \n ", s1, "\n", s2)

#adding the two series

result = s1 + s2
print("Addition: \n", result)

