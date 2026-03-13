#training and running a linear model using scikit learn

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

#download and prepare the data
link = "https://github.com/ageron/data/blob/main"
lifesat = pd.read_csv(link + "/lifesat/lifesat.csv")

X = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values

#visualization of data

lifesat.plot(kind = "scatter", grid = True, x = "GDP per capita (USD)", y = "Life satisfaction")
plt.axis([23_500, 62_500, 4, 9])
plt.show()

#selecting a linear model
model = LinearRegression()

#Train the model
model.fit(X, y)

#make a prediction for Nepal i.e 1154
X_new = [[1_154]]
print(model.predict(X_new))

