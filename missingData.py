import pandas as pd
import numpy as np

d = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}

df = pd.DataFrame(d)

#checking missing values using isnull() method

mv = df.isnull()
print(mv)
