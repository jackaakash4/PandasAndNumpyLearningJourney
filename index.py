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

#setting a custom index

df_with_index = df.set_index('Name')
print("The dataframe with custome index: \n")
print(df_with_index)

#resetig the custom index using rest_index()
print("The dataframe after reseting the custome index: \n")
df_reset = df_with_index.reset_index()
print(df_reset)
