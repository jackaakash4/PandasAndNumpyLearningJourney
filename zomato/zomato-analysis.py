#importing necessary python libraries
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#creating the dataframe
df = pd.read_csv("zomato.csv")

#observing the data
print("\nDataframe\n", df)

#shape of the data
print("\nShape of the data \n", df.shape)

#describing the data
print("\nDescribing the data \n", df.describe())

#data cleaning and preparation
#1. convert the rate column to a float by removing demoninator character

def handleRate(rate):
    rate = str(rate).split('/')
    rate = rate[0];
    return float(rate)

df['rate'] = df['rate'].apply(handleRate)
print("\nAfter converting rate column to float",df.head())
print("\nRate\n", df['rate'])
