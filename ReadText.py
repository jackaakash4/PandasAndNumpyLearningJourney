import pandas as pd

#reading text using read_csv()
df = pd.read_csv("name.txt", sep=" ")

#display dataframe
print(df)

#reading text using read_csv() and header none and names

df1 = pd.read_csv("name.txt", sep = " ", header = None, names = ["Name1", "Name2"])
print("\n",df1)


#reading text using read_table() method here we have to use delimiter

df2 = pd.read_table("name.txt", delimiter = " ")
print("\n",df2)

#reading text file using read_fwf() method

df3 = pd.read_fwf("name.txt")
print("\n", df3)
