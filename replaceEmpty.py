#replace empty string with null and drop null columns

import pandas as pd
import numpy as np

df = pd.DataFrame({'FirstName': ['Vipul', 'Ashish', 'Milan'],
                            "Gender": ["", "", ""],
                            "Age": [0, 0, 0]})

df['Department'] = np.nan
print("Before changing empty string with null \n", df)

df.replace("", np.nan, inplace = True)
print("\nAfter changing\n",df)

#deleting columns with all NaN values
df.dropna(how = 'all', axis = 1, inplace = True)
print("\nAfter deleting columns with all NaN values\n", df)
