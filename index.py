#accessing and modifying the index of dataframe

import pandas as pd

data = {
        'Name': ["Aakash", "Aryan", "Jack"],
        'Address': ["Melamchi", "Indrawati", "America"]
        }

df = pd.DataFrame(data)
print("The result of dataframe: \n")
print(df)

print("The result of index: \n")
print(df.index)
