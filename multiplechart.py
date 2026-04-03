import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4])
y = x * 2

plt.plot(x, y, linestyle = '--', marker = 'x')
plt.title("First line chart")
plt.show()

#new chart
plt.figure()
x1 = [2, 4, 6, 8, 10]
x2 = [1, 2, 3, 4, 5]

plt.plot(x1, x2, '-.')
plt.title("Second line chart")
plt.show()
