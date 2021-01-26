import numpy as np
from matplotlib import pyplot

# +
N = 10 #number of scattered points
x = np.random.normal(0, 5, (N, 2))

fig, axes = pyplot.subplot(aspect='equal')
axes.plot(*x.T)
# -


