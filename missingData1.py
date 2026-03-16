import pandas as pd
import numpy as np
#using isna()
#returns a df of boolean values where True indicates missing data

data = {'Name': ['Amit', 'Sita', np.nan, 'Raj'],
        'Age': [25, np.nan, 22, 28]}

df = pd.DataFrame(data)

print(df.isna())

#checking for non-missing values using notnull()
#not null returns a df with boolean values where True indicate non-missing value

non_missing_value = df.notnull()
print("\nNon missing value")
print(non_missing_value)

#filtering data with non-missing value

csv_data = pd.read_csv("employees.csv")
non_missing_gender = pd.notnull(csv_data["Gender"])

non_missing_gender_data = csv_data[non_missing_gender]
print("\n Non missing gender data")
print(non_missing_gender_data)
