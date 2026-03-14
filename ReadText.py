import pandas as pd

#reading text using read_csv()
df = pd.read_csv("name.txt", sep=" ")

#display dataframe
print(df)

#reading text using read_csv() and header none and names

df1 = pd.read_csv("name.txt", sep = " ", header = None, names = ["Name1", "Name2"])
print("\n",df1)

