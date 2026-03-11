import pandas as pd

#creating a simple dataframe

age = {
        "Name": ["Aakash", "Shrestha"],
        "Age": [23, 24]
        }

df = pd.DataFrame(age)
print("\nAge dataframe\n", df)

#basic export
df.to_csv("age.csv")

#remove index column
df.to_csv("age.csv", index = False)

#export only selected columns
df.to_csv("age.csv", columns = ["Age"])

#exclude the header too
df.to_csv("age.csv", header = False)

#handling the missing data
df.to_csv("age.csv", na_rep = "nothing")


