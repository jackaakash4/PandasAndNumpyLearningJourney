#parsin Json dataset
import pandas as pd
import requests
#converting the dataset to json

df = pd.DataFrame([['a', 'b'], ['c', 'd']],
                  index = ['row 1', 'row 2'],
                  columns = ['col 1', 'col 2']
                  )

print(df.to_json(orient = 'split'))  #separated columns, index and data clearly

print(df.to_json(orient = 'index'))   #show each row as a key-value pair with its index


#read the json file directly from the web

url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)

data = pd.json_normalize(response.json())
print(data.head())
