#importing the package
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#loading dataset
dataset = pd.read_csv("housing.csv")

#checking the dataset
print("Housing dataset: \n", dataset.head())

#Summary of dataset
print("\nSummary of dataset: \n", dataset.describe())
print("\nShape of datset: \n", dataset.shape)
print("\nInfo of dataset: \n", dataset.info())

#since all the features are numeric except ocean_proximity is object. Since it has repetative value it must be categorical value so counting it.

print("\n Count the ocean_proximity's value : \t", dataset['ocean_proximity'].value_counts())

#visualizing the whole dataset

dataset.hist(bins = 64, figsize = (12, 8))
plt.show()
