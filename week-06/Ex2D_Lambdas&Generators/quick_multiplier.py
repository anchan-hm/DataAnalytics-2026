# using lambda function to multiply arguments received

# creating doubler variable
doubler = lambda n: n*2 # double argument

# testing doubler
print(doubler(8)) #output: 16
print(doubler(-4)) #output: -8
print(doubler("banana")) #output: bananabanana

# creating tripler variable
tripler = lambda n: n*3 # triple arguments

# testing tripler
print(tripler(8)) #output: 24
print(tripler(-4)) #output: -12
print(tripler("banana")) #output: bananabananabanana

# creating multiplier variable
def multiplier(num): # multiplier by number
    return lambda n: n*num # returning the multiplied number

# creating similar multiplier variable for 4-10
quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)

# testing multiplier using '2' as test number (can change whenever)
print(quadrupler(2)) #output: 8
print(quintupler(2)) #output: 10
print(sextupler(2)) #output: 12
print(septupler(2)) #output: 14
print(octupler(2)) #output: 16
print(nonupler(2)) #output: 18
print(decupler(2)) #output: 20