#importing necessary python libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#creating the dataframe
dataframe = pd.read_csv("zomato.csv")
print("Original Dataframe \n",dataframe.head())

#cleaning and preparation
#convert the rate column to a float by removing denominator characters

def handleRate(value):
    value = str(value).split('/')
    value = value[0]
    return float(value)

dataframe['rate'] = dataframe['rate'].apply(handleRate)
print("\nAfter change in rate's datatype",dataframe.head())

print("\nDataframe's info: \n", dataframe.info())

#checking for missing or null values to identify any data gaps

print("Any missing value: \n", dataframe.isnull().sum())
