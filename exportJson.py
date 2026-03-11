#exporting pandas df to json file
#using to_json() method

import pandas as pd

df = pd.DataFrame([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']],
                  index=['row 1', 'row 2', 'row 3'],
                  columns=['col 1', 'col 2', 'col 3'])

df.to_json('file.json', orient = 'split', compression = 'infer', index = True)

#now reading the json from same json file
df1 = pd.read_json('file.json', orient = 'split', compression = 'infer')
print(df1)
