#filling missing values

import pandas as pd
import numpy as np

data = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}

df = pd.DataFrame(data)

df1 = df.fillna(0)
print(df1)
