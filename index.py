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

#indexing with loc[]
print("The dataframe after the loc[] is : \n")
row = df_with_index.loc['Aakash']
print(row)

#resetig the custom index using rest_index()
print("The dataframe after reseting the custome index: \n")
df_reset = df_with_index.reset_index()
print(df_reset)

#changing the index
print("After changing the index \n")
df_with_new_index = df.set_index('Address')
print(df_with_new_index)
