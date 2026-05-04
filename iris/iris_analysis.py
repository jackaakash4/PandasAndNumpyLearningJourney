import pandas as pd

#reading the csv file

df = pd.read_csv("iris.csv")

#printing the top rows
print(df.head())

#getting the information about the dataset
print("Information about the dataset\n", df.shape)


print(df.info())

#summary of the dataset
print("\nSummary of the dataset", df.describe())
