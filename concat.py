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

#concatenating df by setting logic on Axes
print("\nConcatenation df by setting logic on Axes")
result1 = pd.concat([df, df1], axis = 1, join = 'outer')
print(result1)

#using inner join
print("\nUsing inner join")
result2 = pd.concat([df, df1], axis = 1, join = 'inner')
print(result2)

#concat df by ignoring indexes
igIndex = pd.concat([df, df1], ignore_index = True)
print("\nConcat df by ignoring indexes")
print(igIndex)

#concat df using group key
groupKey = pd.concat([df, df], keys=['X', 'Y'])
print("\nConcat df using group key")
print(groupKey)


