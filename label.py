#Access an Element in pandas using label

import pandas as pd
import numpy as np

#accessing a single element using index label

data = np.array([1, 2, 3, 4, 5])
ser = pd.Series(data, index = ['a', 'b', 'c', 'd', 'e'])
print("Series: ")
print(ser)
#accessing a element using index element
print("accessing a element using index element")
print("The value at e index is ", ser['e'])

#accessing a multiple element using index element

print("Accessing multiple elemets using index")
print("The value at a, c and d index\n",ser[['a', 'c', 'd']])


#using arange() function 
arange_series = pd.Series(np.arange(1, 10)) 
print("The output of arange() function", arange_series)
