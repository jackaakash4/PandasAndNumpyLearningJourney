#importing packages

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("housing.xlsx")
print("Dataset: \n", df.head())

print("\nShape of dataset \n", df.shape)
