#data processing include data driven work which helps us to provide meaningful insights from the data

#example

import pandas as pd

#loading data in pandas dataframe
data_frame = pd.read_csv("employees.csv")

#printing rows of the data
print(data_frame.head())

print(data_frame.tail())
