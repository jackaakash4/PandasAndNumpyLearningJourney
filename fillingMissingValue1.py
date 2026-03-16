#fill nan values with "no gender"
import pandas as pd

data = pd.read_csv("employees.csv")

data["Gender"].fillna('No Gender', inplace = True)

print("After filling nan value with specific value")
print(data[10:20])
