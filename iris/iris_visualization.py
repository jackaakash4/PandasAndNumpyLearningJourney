import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#importing the iris dataset
df = pd.read_csv("iris.csv")

#Already analzed it so just visualizing

#count plot

sns.countplot(x='species', hue = 'species', data = df)
plt.show()

#relation between variable

#1. comparing sepal length and sepal width
sns.scatterplot(x = 'sepal_length', y = 'sepal_width', hue = 'species', data = df, )

#placing legent outside the frame
plt.legend(bbox_to_anchor = (1, 1), loc = 2)
plt.show()

#2. comparing petal length and petal width
sns.scatterplot(x = 'petal_length', y = 'petal_width', hue = 'species', data = df,)

plt.legend(bbox_to_anchor = (1, 1), loc = 2)
plt.show()


#3. Pairplot

sns.pairplot(df, hue = 'species', height = 2)
plt.show()

#Histograms
fig, axes = plt.subplots(2, 2, figsize = (10, 10))

axes[0, 0].set_title("Sepal Length")
axes[0, 0].hist(df['sepal_length'], bins = 7)

axes[0, 1].set_title("Sepal width")
axes[0, 1].hist(df['sepal_width'], bins = 5)

axes[1, 0].set_title("Petal length")
axes[1, 0].hist(df['petal_length'], bins = 6)

axes[1, 1].set_title("Petal width")
axes[1, 1].hist(df['petal_width'], bins = 6)

plt.show()


#histogram with distplot plot

plot = sns.FacetGrid(df, hue = 'species')
plot.map(sns.displot, 'sepal_length').add_legend()

plot = sns.FacetGrid(df, hue = 'species')
plot.map(sns.displot, 'sepal_width').add_legend()

plot = sns.FacetGrid(df, hue = 'species')
plot.map(sns.displot, 'petal_length').add_legend()

plot = sns.FacedGrid(df, hue = 'species')
plot.map(sns.displot, 'petal_width').add_legend()

plt.show()
