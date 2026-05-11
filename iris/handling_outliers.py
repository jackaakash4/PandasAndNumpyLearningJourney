#importing package
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#load dataset

df = pd.read_csv("iris.csv")
print(df.head())


#visualizing the data in boxplot

sns.boxplot(x = 'sepal_width', data = df)
plt.show()

#in the graph, the values above 4 and below 2 are acting as outliers
#so removing the outliers

#find the IQR

Q1 = np.percentile(df['sepal_width'], 25,
                  )

Q3 = np.percentile(df['sepal_width'], 75,
                   )

IQR = Q3 - Q1

print("Old shape: \n", df.shape)

#upper bound
upper = np.where(df['sepal_width'] >= (Q3 + 1.5 * IQR))

#lower bound 
lower = np.where(df['sepal_width'] <= (Q1 - 1.5 * IQR))

#Removing outliers
df.drop(upper[0], inplace = True)
df.drop(lower[0], inplace = True)

print("New shape: \n", df.shape)

#visualizing after removing the outliers

sns.boxplot(x = 'sepal_width', data = df)
plt.show()
