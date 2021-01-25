import test
import numpy as np
import matplotlib.pyplot as plt

radius = 10
area = test.area(radius)

print('Area is = ', area)

[x,y] = test.drawcircle(radius)

fig, axes = plt.subplots()
axes.plot(x, y)
axes.plot(x, -y)

fig.savefig('circle.png')