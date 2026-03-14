import pandas as pd

#reading the csv file from the url
url = "https://github.com/ageron/data/blob/main/lifesat/lifesat_full.csv"
df = pd.read_csv(url)
print(df)
