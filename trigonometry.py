#plotting trigonometric functions in matplot

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin, label = "sin(x)")
plt.plot(x, y_cos, label = "cos(x)")

plt.fill_between(x, y_sin, y_cos, color = "green", alpha = 0.4)

plt.title("Trigonometric function")
plt.xlabel("X values")
plt.ylabel("Function value")
plt.legend()
plt.show()
