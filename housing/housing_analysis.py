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
