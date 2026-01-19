#filter pandas dataframe with multiple conditions

import pandas as pd
import numpy as np

df = pd.DataFrame(
        {
            'Name': [' RACHEL  ', ' MONICA  ', ' PHOEBE  ',
                                   '  ROSS    ', 'CHANDLER', ' JOEY    '],
                          
                          'Age': [30, 35, 37, 33, 34, 30],
                          
                          'Salary': [100000, 93000, 88000, 120000, 94000, 95000],
                          
                          'JOB': ['DESIGNER', 'CHEF', 'MASUS', 'PALENTOLOGY',
                                  'IT', 'ARTIST']
        }
    )

print("\nDataset: ")
print(df)

#filter dataframe with multiple conditions using loc
print("\nFiltering dataframe with multiple condditions using loc ")
print(df.loc[(df['Salary'] >= 90000) & (df['Age']  < 40) & (df['JOB'].str.startswith('D')), ['Name', 'JOB']])


#filter dataframe using numpy
print("\nFiltering dataframe with multiple conditions using numpy")
filtered_value = np.where((df['Age'] > 30) & (df['Salary'] > 80000))
print(filtered_value)
print(df.loc[filtered_value])

#filter dataframe using query
#query and eval works onnly with columns
print("\nFiltering dataframe with multiple conditions using query")
print(df.query('Salary > 90000 & Age > 40'))


