import matplotlib.pyplot as plt

a = [1, 2, 3, 4, 5]
b = [0, 0.6, 0.2, 15, 10, 8, 16, 21]
c = [4, 2, 6, 8, 3, 20, 13, 15]

fig = plt.figure(figsize = (10, 10))

sub1 = plt.subplot(2, 2, 1)
sub2 = plt.subplot(2, 2, 2)
sub3 = plt.subplot(2, 2, 3)
sub4 = plt.subplot(2, 2, 4)

sub1.plot(a, 'sb')
sub2.plot(b, 'or')
sub3.plot(c, 'Dm')
sub4.plot(list(range(0, 22, 3)), 'vg')

plt.show()
