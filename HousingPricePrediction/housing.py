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
