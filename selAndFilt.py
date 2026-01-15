import pandas as pd


df = pd.read_csv("people_data.csv")

print(df.head())

#selecting and filtering
print("\nAfter filtering")
sex = df[df['Sex'] == 'Male']
print(sex)

#adding the new column
print("\nAfter adding new column")
df['Full Name'] = df['First Name'] +" "+ df['Last Name']
print(df.head())
