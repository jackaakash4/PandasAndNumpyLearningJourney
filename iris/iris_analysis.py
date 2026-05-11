import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#reading the csv file

df = pd.read_csv("iris.csv")

#printing the top rows
print(df.head())

#getting the information about the dataset
print("\nInformation about the dataset\n", df.shape)


print(df.info())

#summary of the dataset
print("\nSummary of the dataset\n", df.describe())

#checking the missing value
#using isnull()

print("\nChecking the missing value \n", df.isnull().sum())

#checking the duplicates value

data = df.drop_duplicates(subset = 'species',)
print("\nAfter dropping the duplicates:\n", data)

#checking the number of element in each species
print("\nChecking the species number count\n", df.value_counts('species'))

#data visualization

sns.countplot(x='species', data = df)
plt.show()

#pairwire relationships in dataset using seaborn
iris = sns.load_dataset("iris")
sns.pairplot(iris, hue = "species")
plt.show()




