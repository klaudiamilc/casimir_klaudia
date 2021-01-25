print('Hello world')
print('Hi')

import numpy as np

def area(radius):
        a = np.pi*radius**2
        return(a)
    
a = area(10)
print(a)

def circumference(radius):
	c=2*np.pi*radius
	return(c)
