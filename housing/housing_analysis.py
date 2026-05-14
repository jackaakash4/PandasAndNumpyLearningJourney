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
        axis = 1, 
        inplace = True
        )


#replacing SalePrice empty values with their mean
df['SalePrice'] = df['SalePrice'].fillna(df['SalePrice'].mean())


#drop records with null values(because empty records are very less)
new_df = df.dropna()

#checking the nullvalues in the new dataframe
print("Checking the null values of new dataframe \n", new_df.isnull().sum())


#OneHotEncoder: For label categorical features
#it is the best way to convert categorical data into binary vectors. This maps the values to integer values.
#using it, we can easily convert object data into int

from sklearn.preprocessing import OneHotEncoder

s = (df.dtypes == 'object')
object_cols = list(s[s].index)
print("Categorical variables: \n", object_cols)
print("\nNo. of categorical variables: \n", len(object_cols))

#after listing all the features. now OneHotEncoding to the whole list

OH_encoder = OneHotEncoder(sparse_output = False, handle_unknown = 'ignore')
OH_cols = pd.DataFrame(OH_encoder.fit_transform(df[object_cols]))
OH_cols.index = df.index
OH_cols.columns = OH_encoder.get_feature_names_out()
df_final = df.drop(object_cols, axis = 1)
df_final = pd.concat([df_final, OH_cols], axis = 1)

print("\nFinal dataframe: \n", df_final)
print("\nDescribe final datafram: \n", df_final.describe())
print("\nInfo of final dataframe: \n", df_final.info())
print("\nShape of final dataframe: \n", df_final.shape)






























