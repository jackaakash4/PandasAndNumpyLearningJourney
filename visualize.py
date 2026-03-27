import pandas as pd
import matplotlib.pyplot as plt
#importing csv file's data

data = pd.read_csv("employees.csv")

dataframe = pd.DataFrame(data)
print("Dataframe: \n", dataframe)

#summary of df
print("\nSummary of df: \n", dataframe.info())

#Detail of df
print("\nDetail of df: \n", dataframe.describe())

#Ploting the histogram
dataframe.plot(kind = 'bar')
plt.show()
