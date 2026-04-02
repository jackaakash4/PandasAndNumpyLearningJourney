import numpy as np
import matplotlib.pyplot as plt

days = ['Sun', 'Mon', 'Tue', 'Wed','Thu', 'Fri']
temperature = [22, 25, 21, 22, 27, 30]

plt.plot(days, temperature, marker = 'o')

plt.title('Weekly temperature')
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.show()
