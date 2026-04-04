#line chart with annotations using annotate() function

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.figure()
plt.plot(x, y, marker = 'o', linestyle = '-')

for xi, yi in zip(x, y):
    plt.annotate(f'({xi}, {yi})',
                (xi, yi),
                 textcoords = 'offset points',
                 xytext = (0, 10),
                 ha= 'center'
                 )

plt.title('Line chart with annotations')
plt.xlabel('X----->')
plt.ylabel('Y----->')
plt.grid(True)
plt.show()
