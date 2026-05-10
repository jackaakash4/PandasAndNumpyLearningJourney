#importing packages

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("housing.xlsx")
print("Dataset: \n", df.head())

print("\nShape of dataset \n", df.shape)
print("\nSummary of dataset \n", df.describe())

#dataprocessing
#categorizing the features based on their data types

object_cols = df.select_dtypes(include = ['object']).columns
print("Categorical variables: ", len(object_cols), "\t", object_cols)

int_cols = df.select_dtypes(include = ['int64']).columns
print("Integer variables: ", len(int_cols), "\t", int_cols)

float_cols = df.select_dtypes(include = ['float64']).columns
print("Float variables: ", len(float_cols), "\t", float_cols)

#heat map
#selecting the numerical feature for heatmap

numerical_df = df.select_dtypes(include = ['int64', 'float64'])

plt.figure(figsize = (12, 6))
sns.heatmap(numerical_df.corr(),
            annot = True,
            fmt = '.2f',
            linewidths = 2,
            cmap = 'BrBG'
            )
plt.title("Corellation heatmap of numerical features")
plt.tight_layout()
plt.show()

#To examine the categorical features, creating Barplot to visualize the distribution

unique_value  = []

for col in object_cols:
    unique_value.append(df[col].unique().size)

plt.figure(figsize = (10, 6))

plt.title("Number of unique values of categorical feature \n")
plt.xticks(rotation = 90)
sns.barplot(x = object_cols, y = unique_value)
plt.show()

#bargraph of each four features separately

plt.figure(figsize = (18, 36)) 
plt.title("Categorical features: distribution")
plt.xticks(rotation = 90)
index = 1

for col in object_cols:
    y = df[col].value_counts()
    plt.subplot(11, 4, index)
    plt.xticks(rotation = 90)
    sns.barplot(x = list(y.index), y = y, hue = list(y.index),)
    index +=1
    plt.show()

#Data Cleaning

#dropping the id column, because it will not be participation in any prediction

df.drop(['Id'],
        axix = 1, 
        inplace = True
        )


#replacing SalePrice empty values with their mean

df['SalePrice'] = df['SalePrice'].fillna(df['SalePrice'].mean())































