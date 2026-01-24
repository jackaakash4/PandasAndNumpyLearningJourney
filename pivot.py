#creating a simple dataframe and pivot tablle

import pandas as pd

df = pd.DataFrame(
        {
            
            'Product': ['Carrots', 'Broccoli', 'Banana', 'Banana', 'Beans', 'Orange', 'Broccoli', 'Banana'],
            'Category': ['Vegetable', 'Vegetable', 'Fruit', 'Fruit', 'Vegetable', 'Fruit', 'Vegetable', 'Fruit'],
                   'Quantity': [8, 5, 3, 4, 5, 9, 11, 8],
                   'Amount': [270, 239, 617, 384, 626, 610, 62, 90]})

print("Dataframe: \n")

print(df)


#get the total sales of each product by creating pivot table

pivot = df.pivot_table(
            index = ['Product'],
            values = ['Amount'],
            aggfunc = 'sum')
print("\nPivot Table")

print(pivot)

#get the total sales of each category
pivot1 = df.pivot_table(
            index = ['Category'],
            values = ['Amount'],
            aggfunc = ['sum']
            )
print("\nThe total sales of each category")
print(pivot1)


#get total sales by category and product both

pivot2 = df.pivot_table(
            index = ['Category', 'Product'],
            values = ['Amount'],
            aggfunc = ['sum']
            )
print("\nTotal sale by category and product both")
print(pivot2)


#get the mean. median, minimum sales by category

pivot3 = df.pivot_table(
            index = ['Category'],
            values = ['Amount'],
            aggfunc = ['median', 'min']
            )
print("\nMedian and minimum sales by category")
print(pivot3)


#get the mea, median, minimum sales by product

pivot4 = df.pivot_table(
            index = ['Product'],
            values = ['Amount'],
            aggfunc = ['mean', 'median', 'min']
            )
print("\n the mean. median and minimum sales by product")
print(pivot4)

