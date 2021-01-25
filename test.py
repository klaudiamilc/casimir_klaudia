
print('Hello world')
print('Hi')

import numpy as np

def area(radius):
    a = np.pi*radius**2
    return(a)

def circumference(radius):
	c=2*np.pi*radius
	return(c)

def drawcircle(radius):
    x = np.linspace(-radius, radius, 100)
    y = np.sqrt(radius**2-x**2)
    return[x, y]