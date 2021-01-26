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
print(angles)
print(index_min)
print (scattered_points[index_min])
print(type(arr))



# -

scattered_points[0][1]
