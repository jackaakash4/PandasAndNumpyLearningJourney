import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = x * 2

x1 = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]

plt.plot(x, y, marker= 'x', linestyle='-', label = 'y = 2x')
plt.plot(x1, y1, '--', label = 'y = x^2')

plt.xlabel('X-axix')
plt.ylabel('Y-axis')
plt.title("Multiple plots on same axis")
plt.legend()
plt.show()
