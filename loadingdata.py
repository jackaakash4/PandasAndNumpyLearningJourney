import pandas as pd

df = pd.read_csv("people_data.csv")

#head() shows only first 5 rows of data
print(df.head())


#to get info
print(df.info())


#handling missing data
print("Handling missing data \n")
print(df.isnull().sum())


#filling the emply with )
df = df.fillna(0)

