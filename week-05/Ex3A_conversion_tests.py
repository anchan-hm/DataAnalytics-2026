# Description: This script tests various numeric
#               conversion techniques
# Author: Sam Q. Newprogrammer

# defining variables
a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# testing transformations

# for a
a_float = float(a)  #works
# a_int = int(a)   #ValueError: invalid literal for int()
a_int_float = int(float(a))  #works
print(a.strip())    #stripped spaces, output: 101.1
print(a, type(a)) # output: 101.1  <class 'str'>

# for b
b_int = int(b)   #works
b_float = float(b)  #works
print(b, type(b)) #output: 55 <class 'str'>

# for c
# c_int = int(c)   #ValueError: invalid literal for int()
# c_float = float(c)  #ValueError: cannot convert to a float
c_slice = c[0:3]   #slicing "402"
print(c_slice)  #output: 402
c_slice_int = int(c_slice) #works
print(c_slice_int)  #output: 402
print(c, type(c))  #output: 402 Stevens <class 'str'>

# for d
# d_int = int(d)  #ValueError: invalid literal for int()
# d_float = float(d)   #ValueError: cannot convert to a float
d_slice = d[-2]  #slicing to have "5"
print(d_slice)  #output: 5
d_slice_int = int(d_slice)  #works
print(d_slice_int) #output: 5
print(d.strip())  #output: Number 5
print(d, type(d))  #output: Number 5  <class 'str'>

# printing new variables
print(a_float, type(a_float))  #output: 101.1 <class 'float'>
print(b_int, type(b_int))    #output: 55 <class 'int'>
print(b_float, type(b_float))  #output: 55.0 <class 'float'>
print(c_slice_int, type(c_slice_int))   #output: 402 <class 'int'>
print(d_slice_int, type(d_slice_int))  #output: 5 <class 'int'>