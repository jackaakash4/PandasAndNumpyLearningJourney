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

#creating a training and test sets
def shuffle_and_split(data, ratio, rnd):
    shuffled_indices = rnd.permutation(len(data))
    test_set_size = int(ratio * len(data))
    test_indices = shuffled_indices[:test_set_size]
    training_indices = shuffled_indices[test_set_size:]
    print("Shuffled_indices: \t", shuffled_indices, "\t Test set indices: \t", test_indices, "\tTraining set indices: \t", training_indices)
    return data.iloc[test_indices], data.iloc[training_indices]


#generate random number
rng = np.random.default_rng()
testing_set, training_set = shuffle_and_split(dataset, 0.2, rng)
print(f"Length of training set is : {len(training_set)} and testing set is : {len(testing_set)}")



#creating the training and tests set using scikit learn

from sklearn.model_selection import train_test_split

train_set, test_set = train_test_split(dataset, test_size = 0.2, random_state = 42)
#this is same as shuffle and split and can generate same dataset using random state
print(f"Length of training and testing set using train_test_split method: {len(train_set)} and {len(test_set)}")
