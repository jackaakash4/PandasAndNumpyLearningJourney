#Binary operations on series

import pandas as pd

s1 = pd.Series([10, 9, 8], index = ['a', 'b', 'c'])
s2 = pd.Series([1, 2 ,3], index = ['a', 'b', 'c'])
#printing the series
print("Series: \n ", s1, "\n", s2)

#adding the two series

result = s1 + s2
print("Addition: \n", result)

#comparison operations on series
ser1 = pd.Series([10, 20, 30])
ser2 = pd.Series([10, 20, 30])

print("Comparing two series")
print(s1 == s2)
