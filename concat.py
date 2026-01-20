#concate two dataframe

import pandas as pd

data1 = {
        'Name': ["Aakash", "Jack", "Shrestha"],
        'Age': [23, 15, 30],
        'Address': ["Melamchi", "America", "Indrawati"]
        }
data2 = {
        'Name': ["Aryan", "John", "HHH"],
        'Age': [19, 45, 50],
        'Address': ["Sindhupalchok", "Texas", "LA"]
        }

df = pd.DataFrame(data1, index=[0, 1, 2])

df1 = pd.DataFrame(data2, index=[3, 4, 5])

print(df, "\n\n", df1)

#concating using .concat function

frames = [df, df1]

result = pd.concat(frames)
print("\n", result)
