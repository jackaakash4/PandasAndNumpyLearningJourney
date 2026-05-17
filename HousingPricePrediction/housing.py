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

#visualizing the median income
#creating new catagory income_cat

dataset['income_cat'] = pd.cut(dataset['median_income'],
                               bins = [0., 1.5, 3.0, 4.5, 6., np.inf],
                               labels = [1, 2, 3, 4, 5])

cat_counts = dataset['income_cat'].value_counts().sort_index()
cat_counts.plot.bar(rot = 0, grid = False)
plt.xlabel("Income category")
plt.ylabel("No. of districts")
plt.show()

#now creating 10 different stratified splits of the same dataset
from sklearn.model_selection import StratifiedShuffleSplit

splitter = StratifiedShuffleSplit(n_splits = 10, test_size = 0.2, random_state = 42)
strat_splits = []

for train_index, test_index in splitter.split(dataset, dataset['income_cat']):
    strat_train_set_n = dataset.iloc[train_index]
    strat_test_set_n = dataset.iloc[test_index]
    strat_splits.append([strat_train_set_n, strat_test_set_n])

strat_train_set, strat_test_set = strat_splits[0]

print("Strat test set: \n", strat_test_set['income_cat'].value_counts() / len(strat_test_set))

#deleting the income category

for set_ in (strat_train_set, strat_test_set):
    set_.drop("income_cat", axis = 1, inplace = True)


#Exploring and Visualizing the data to gain insight
housing = strat_train_set.copy()

#visualizing geographical data

housing.plot(kind = 'scatter', x = 'longitude', y = 'latitude', grid = True, alpha = 0.2)
plt.show()


housing.plot(kind = 'scatter', x = 'longitude', y = 'latitude', grid = True, s = housing['population'] / 100, label = 'population', c = 'median_house_value', cmap = 'jet', colorbar = True, legend = True, sharex = False, figsize = (10, 7))
plt.show()

#Look for correlation
#since the dataset is not too large, we can easily compute the standard correlation coefficient between every pair of numerical attributes using corr() method

corr_matrix = housing.corr(numeric_only = True)
#looking how much each attribute correlates with the median house value
print("Correlation between median house value with other attributes: \n", corr_matrix['median_house_value'].sort_values(ascending=False))
sns.pairplot(data = corr_matrix)
plt.show()

#plotting correlation between attributes using scatter_matrix() method

from pandas.plotting import scatter_matrix

attributes = ['median_house_value', 'median_income', 'total_rooms', 'housing_median_age']

scatter_matrix(housing[attributes], figsize = (12, 8))
plt.show()

#plotting the housing dataset between median_income and median_house_value

housing.plot(kind = 'scatter', x = 'median_income', y = 'median_house_value', alpha = 0.1, grid = True)
plt.show()
