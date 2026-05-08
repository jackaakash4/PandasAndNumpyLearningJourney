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
