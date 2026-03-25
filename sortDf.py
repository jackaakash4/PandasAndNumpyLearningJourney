import pandas as pd


data = pd.read_csv("employees.csv")
df = pd.DataFrame(data)

print("Dataframe : \n", df.head())


#sorting value using sort_values()

print("After sorting: \n", df.sort_values(by = "First Name", ascending = True).head())
