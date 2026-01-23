#merging DataFrame
import pandas as pd

data1 = {
        'id': [1, 2, 3, 4, 5, 6],
        'Name': ["Aakash", "Shrestha", "HHH", "John", "Chris", "Punk"],
        'Age': [23, 45, 34, 23, 44, 76],
        }

data2 = {
        'id': [1, 2, 3, 4, 5, 6],
        'Address': ["LA", "NY", "Texas", "Ktm", "Pokhara", "Jhapa"],
        'Qualification': ["Btech", "BA", "Bcom", "B.hons", "BSc", "BIT"]
        }

df = pd.DataFrame(data1)
df1 = pd.DataFrame(data2)

print("Dataframe: ")
print(df, "\n", df1)

#merging using .merge() with one unique key combination

result = pd.merge(df, df1, on='id')
print("Merging using id")
print(result)
