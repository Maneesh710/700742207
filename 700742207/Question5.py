#Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
import numpy
radius=30
pi=3.14
_area_of_circle_=pi*pow(radius,2)
print(_area_of_circle_)

#Calculate the circumference of a circle and assign the value to a variable name of _circum_of_circle_
_circum_of_circle_=2*pi*radius
print(_circum_of_circle_)

#Take radius as user input and calculate the area.
r=input('Enter the radius:')
r=int(r)
area=pi*pow(r,2)
print(area)