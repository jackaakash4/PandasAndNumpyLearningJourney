#data processing include data driven work which helps us to provide meaningful insights from the data

#example

import pandas as pd

#loading data in pandas dataframe
data_frame = pd.read_csv("employees.csv")

#printing rows of the data
print("Dataframe's head: \n",data_frame.head())

print("Dataframe's tail: \n",data_frame.tail())

#printing the column names of the dataframe

print("Columns name of the dataframe \n", list(data_frame.columns))

#summary of the dataframe

print("The summary of the dataframe is \n", data_frame.info())

#descriptive statistical measures of a dataframe
print("The descriptive statistical measures of a dataframe is \n", data_frame.describe())

#handling missing data
#find missing values in the dataset using isnull() to detect the missing values

print("Finding the null value in dataframe: \n", data_frame.isnull())

#finding the number of missing values in the dataset
print("Finding the no of missing values in the dataset: \n", data_frame.isnull().sum())

