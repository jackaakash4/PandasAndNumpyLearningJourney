import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([1, 2, 3, 4, 5])
x2 = x1 ** 2

plt.scatter(x1, x2, color = "red", label = "Group 1")
plt.scatter(x2, x1, color = "blue", label = "Group 2")

plt.xlabel("Value of x")
plt.ylabel("y = x^2")
plt.title("y = x^2 graph")

plt.legend()
plt.show()
