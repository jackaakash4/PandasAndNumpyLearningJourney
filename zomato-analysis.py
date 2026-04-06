#importing necessary python libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#creating the dataframe
dataframe = pd.read_csv("zomato.csv")
print(dataframe.head())
