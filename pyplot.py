#matplotlib Pyplot
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]


fig, ax = plt.subplots()
ax.plot(x, y, marker= 'o', label="Data Points")

ax.set_title("Basic components of Matplotlib Figure")
ax.set_xlabel("X-Axis")
ax.set_ylabel("Y-Axis")

plt.show()
