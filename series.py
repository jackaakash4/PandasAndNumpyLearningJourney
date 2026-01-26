import pandas as pd
import numpy as np

s = pd.Series()
print("Pandas Series: ", s)

data = np.array(['J', 'A', 'C', 'K'])

s = pd.Series(data)
print("Pandas Series: \n", s)

#creating a series from a dictionary

data_dict = {
        'name': "Aakash",
        'age': 23,
        'address': "Melamchi"
        }

print("Series from a dictionary \n")

series_dict = pd.Series(data_dict)
print(series_dict)

#creating a series using numpy function

ser = pd.Series(np.linspace(1, 10, 5))
print("\nSeries using numpy function linspace")
print(ser)


#creating a series using range()

series_range = pd.Series(range(1, 10))
print("\nCreating a series using range()")
print(series_range)

#creating a series using list comprehension
#way to generate sequences and apply transformation in a single line of code

list_comp = pd.Series(range(1, 20, 5), index = [x for x in 'abcd'])
print("List comprehension")
print(list_comp)


#Accessing the series
#accessing the first element
print("\nAccessing the first element")
print(s[0])

#accessing the first 5 element
print("\nAccessing the first 5 element")
print(s[:5])

#Accessing the last 4 elements
print("\nAccessing the last 4 elements")
print(list_comp[-4:])

#Acessing first five elements of series in csv file

df = pd.read_csv("people_data.csv")
csv_ser = pd.Series(df['First Name'])
print("\nFirst five elements of series in csv file")
print(csv_ser.head(5))

