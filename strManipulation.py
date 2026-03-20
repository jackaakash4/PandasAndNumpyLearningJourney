#string manipulations in pandas dataframe
import pandas as pd
import numpy as np

data = { 'Name': ['Lukas', 'Sofia', 'Hiroshi', 'Marta', 'Yannis', np.nan, 'Elena'],
         'City': ['Berlin', 'Madrid', 'Tokyo', 'Warsaw', 'Athens', 'Oslo', 'Lisbon'] }

df = pd.DataFrame(data)
print("Dataframe: \n", df)


#string ooperations in pandas

#columns to lowercase using lower()

print("\nChanging Name field to lowercase \n",df["Name"].str.lower())

#columns to uppercase using upper()
print("\nChanging City field to uppercase \n", df["City"].str.upper())

#removes unwanter leading and trailing spaces using strip()

print("\nRemoving unwanted leading and trailing spaces using strip()\n", df["Name"].str.strip()) 

#split() method split each string into a list of parts based on a given separator
print("\n Splitting string \n", df["Name"].str.split('a'))

#len() method to calculate the length of string
print("\n Counting the length of string \n", df["Name"].str.len())
