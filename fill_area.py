import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = x **2

y1 = [1, 3, 5, 7, 9]

plt.plot(x, y, label = 'y = x^2')
plt.plot(x, y1, label = 'y1')

plt.fill_between(x, y, y1, color = 'blue', alpha = 0.4)

plt.title("Area filled between two lines")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()
