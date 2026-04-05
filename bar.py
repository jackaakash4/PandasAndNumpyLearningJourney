import matplotlib.pyplot as plt
import numpy as np

fruits = ["Apples", "Bananas", "Grapes", "Orange"]
sales = [500, 200, 300, 120]

plt.bar(fruits, sales)
plt.title("Fruits sale")
plt.xlabel("Fruits")
plt.ylabel("Sales")
plt.show()
