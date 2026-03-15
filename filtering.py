import pandas as pd

data = pd.read_csv("employees.csv")

print(data)

#filtering data based on missing values
bool_series = pd.isnull(data["Gender"])
missing_gender_data = data[bool_series]
print("Missing gender data \n")
print(missing_gender_data)
