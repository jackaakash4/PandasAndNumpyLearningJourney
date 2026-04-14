import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(50, 150, 100)
y = np.random.randint(20, 150, 100)

colors = np.random.rand(100)
size = 20 * np.random.randint(10, 100, 100)

plt.scatter(x, y, c = colors, s = size, cmap='viridis', alpha = 0.7)
plt.colorbar(label = 'Color scale')
plt.title("Scatter plot with color map and color bar")
plt.show()
