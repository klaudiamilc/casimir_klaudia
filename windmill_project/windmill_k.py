import numpy as np
import matplotlib.pyplot as plt
from numpy import ones,vstack
from numpy.linalg import lstsq
from matplotlib.animation import FuncAnimation

N = 1 #number of scattered points
x = np.random.normal(0, 5, (N, 2))


# +
# creating a line
point = 0
start_point = x[point, :] # choose a starting point must be <N
line_x = np.linspace(x[point, 0]-100, x[point, 0]+100)

# points = [rot_point, x[point, :]]
# x_coords, y_coords = zip(*points)
# A = vstack([x_coords,ones(len(x_coords))]).T
# m, c = lstsq(A, y_coords, rcond = -1)[0] #m is the slope, c is the interceptb
m = 0
c = start_point[1]-m*start_point[0]
line_y = m*line_x+c

fig, axes = plt.subplots()
axes.scatter(*x.T)
axes.plot(line_x, line_y, color='k')
axes.scatter(start_point[0], start_point[1])
axes.set_xlim(np.min(x[:, 0])-10, np.max(x[:, 0])+10)
line, = axes.plot([], [], lw=3)

def init():
    line.set_data([], [])
    return line,
def animate(i):
    r = 10
    x = line_x
    y = np.sqrt(np.abs(r**2-x**2))
    line.set_data(x, y)
    return line,

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

anim.save('rot_line.gif', writer='imagemagick')


# +
def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

angles = []
for i in range(len(x)):
    compared_points = ((start_point),(x[i, 0],x[i, 1]))
    y = angle_between(compared_points[0],compared_points[1])
    angles.append(y)
arr = np.array(angles)

srt = np.argsort(arr) # returns indices for sorted angles, index 1 is the next one after 0
smallest = np.where(srt == 0)
smallest_angle = arr[smallest] # smallest angle after 0
point_coord = x[2] #coordinates of the point which has the smallest angle to the current centre of rot.
print(point_coord)
# -

print(angles)

print(smallest_angle)

fig, axes = plt.subplots()
axes.scatter(*x.T)
axes.scatter(start_point[0], start_point[1])
axes.scatter(point_coord[0], point_coord[0])


