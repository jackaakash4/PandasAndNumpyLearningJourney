#importing necessary python libraries
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#creating the dataframe
df = pd.read_csv("zomato.csv")

#observing the data
print("\nDataframe\n", df)

#shape of the data
print("\nShape of the data \n", df.shape)

#describing the data
print("\nDescribing the data \n", df.describe())

#data cleaning and preparation
#1. convert the rate column to a float by removing demoninator character

def handleRate(rate):
    rate = str(rate).split('/')
    rate = rate[0];
    return float(rate)

df['rate'] = df['rate'].apply(handleRate)
print("\nAfter converting rate column to float",df.head())
print("\nRate\n", df['rate'])

#summarize the dataframe
print("\nSummary of the dataframe \n", df.info())


#checking for missing value
print("\nChecking for missing values or null valuus \n", df.isnull().sum())

#visualizing the dataset

sns.countplot(x = df['listed_in(type)'], hue = df['listed_in(type)'],)
plt.xlabel("Types of restaurant")
plt.ylabel("No. of restuarant")

plt.show()

#votes by restaurant type

grouped_data = df.groupby('listed_in(type)')['votes'].sum()

result = pd.DataFrame({'votes': grouped_data})
plt.plot(result, c = 'green', marker = 'x')
plt.xlabel('Types of restaurant')
plt.ylabel('votes')
plt.show()


#identify the most voted  restaurant

max_votes = df['votes'].max()

rest_with_max_votes = df.loc[df['votes'] == max_votes, 'name']

print('Restaurant with the maximum votes:', rest_with_max_votes)




#online order availability
sns.countplot(x = df['online_order'], hue = df['online_order'])
plt.show()


#analze rating
plt.hist(df['rate'], bins = 10)
plt.title("Rating distribution")
plt.show()


#approximate cost for couple
couple_data = df['approx_cost(for two people)']
sns.countplot(x = couple_data, hue = couple_data)
plt.show()

#rating comparison - online vs offline order

plt.figure(figsize = (6, 6))
sns.boxplot(x = 'online_order', y = 'rate',hue = 'online_order', data = df)
plt.show()

#order mode preferences by restaurant type
pivot_table = df.pivot_table(index = 'listed_in(type)', columns = 'online_order', aggfunc = 'size', fill_value = 0)

sns.heatmap(pivot_table, annot = True, cmap = 'YlGnBu', fmt = 'd')
plt.title('Heatmap')
plt.xlabel("Online order")
plt.ylabel("Listed In (type)")
plt.show()
