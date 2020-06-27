#!/usr/bin/env python3

from math import pi

h = 5.0 #height
b=2.0 #base
r = 1.5 #radius

area_parallelogram = h*b 
print('the area of the paralelogram is %.3f' % area_parallelogram)

area_square = b**2
print('the area of the square is %g' % area_square)

area_circle = pi*r**2
print('the area of the circle is %8.3f' % area_circle)

volume_cone = 1.0/3*pi*r**2*h
print('the volume of the cone is %.3f' % volume_cone)

