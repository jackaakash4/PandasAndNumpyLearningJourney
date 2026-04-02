import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4])
y = x ** 2

plt.title("Simple line plot with label")

plt.xlabel("x")
plt.ylabel("y = x^2")
plt.plot(x, y, marker = 'o', linestyle = '--', label = 'Datapoint')
plt.legend()
plt.show()


