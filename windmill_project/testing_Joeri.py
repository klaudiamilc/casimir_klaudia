# +
# %matplotlib widget
import numpy as np
from matplotlib import pyplot
N = 10 #the number of points
scattered_points = np.random.random((N,2))
print(type(scattered_points))
print(scattered_points)
pyplot.subplot(aspect='equal')
pyplot.scatter(*scattered_points.T)

starting_slope = [1,0]
starting_point = [0,0]



slopes_to_origin = scattered_points[:,1]/scattered_points[:,0]
angle_to_origin = np.arctan(((import numpy as np

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
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))1-0)/(1+0*1)))
print('angle is ' + str(angle_to_origin))
print(slopes_to_origin)
print(closest_point)

#slope_combinations
#for i in slopes_to_origin:
 #   slope_between_lines = 





# +
# %matplotlib widget
import numpy as np
from matplotlib import pyplot

N = 10 #the number of points
scattered_points = np.random.random((N,2))

print(scattered_points)

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



compared_points = ((scattered_points[0][0],scattered_points[0][1]),(scattered_points[1][0],scattered_points[1][1]))

angles = []
for i in range(len(scattered_points)-1):
    compared_points = ((scattered_points[0][0],scattered_points[0][1]),(scattered_points[i+1][0],scattered_points[i+1][1]))
    y = angle_between(compared_points[0],compared_points[1])
    angles.append(y)
    
arr = np.array(angles)
index_min = np.argmin(arr)
updated_location_and_slope = [scattered_points[index_min],angles[index_min]]
print(angles)
print(index_min)
print(updated_location_and_slope)
print (scattered_points[index_min],angles[index_min])
print(type(arr))



# +
# %matplotlib widget
import numpy as np
import matplotlib.pyplot as plt
from numpy import ones,vstack
from numpy.linalg import lstsq
from matplotlib.animation import FuncAnimation

N = 5
x = np.random.normal(0, 5, (N, 2))
x0 = [0,0]


# +
def closest_point(x0,x):
    combination_data = []
    for xi in x:
        r = ((x0[0]-xi[0])**2+(x0[1]-xi[1])**2)**0.5
        delta_y = (x0[1]-xi[1])
        sin_angle = (delta_y/r)
        combination_data.append(sin_angle)
    min_angle = min(combination_data)
    search_list = np.array(combination_data)
    index_smallest = np.where(search_list==min_angle)
    new_point = x[index_smallest[0][0]]
    return new_point

fig, axes = plt.subplots()
axes.scatter(*x.T)
axes.scatter(*x0)

print(x)
y = closest_point(x0,x)
axes.scatter(*y)
print(y)

