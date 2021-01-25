
print('Hello world')
print('Hi')

import numpy as np

def area(radius):
	'''
	This fucntion calculates the area of a circle with radiu R
	
	'''
    a = np.pi*radius**2
    return(a)

def circumference(radius):
	c=2*np.pi*radius
	return(c)
