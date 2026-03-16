import pandas as pd
import numpy as np
#using isna()
#returns a df of boolean values where True indicates missing data

data = {'Name': ['Amit', 'Sita', np.nan, 'Raj'],
        'Age': [25, np.nan, 22, 28]}

df = pd.DataFrame(data)

print(df.isna())
