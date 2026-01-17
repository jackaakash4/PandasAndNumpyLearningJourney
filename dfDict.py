import pandas as pd
import numpy as np


data = np.array([[1, 2, 3], [2, 3, 4], [5, 6, 7]])

df = pd.DataFrame(data, columns = ['A', 'B', 'C'])
print(df)
