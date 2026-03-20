#dropping empty columns in pandas
#dropna() function

import pandas as pd
import numpy as np

df = pd.DataFrame({
        "FirstName": ["Aakash", "Aryan", "Abishek"],
        "Gender": ["", "", ""],
        "Age": [0, 0, 0]
        })

df['Department'] = np.nan
print(df)


