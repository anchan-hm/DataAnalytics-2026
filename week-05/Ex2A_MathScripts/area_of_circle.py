# calculating the area of a circle
#importing library
import math

# using birth day for the diameter
diameter = 20 # day
radius = diameter/2 # radius is half of a diameter

# calculating the area
area = math.pi*(radius**2)

# displaying the results with f-string
print(f"The area of the circle with radius {radius} is {area:.2f}")
# The area of a circle with radius 10.0 is 314.1592653589793