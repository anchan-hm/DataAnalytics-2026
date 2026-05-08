# creating variables
x = 100
y = 20

# using if block
# 3a
if x/y == 5:
    print("x divided by y is 5")
    x = 1
else:
    print("are the variables set up correctly?") #output: x divided by y is 5

# 3b
if x*y == y:
    print("now x times y is y")
    x = 10 
else:
    print("Whoops, x equals", x) #output: now x times y is y

# 3c
if x < y:
    print("x is less than y")
    x = x*2
else:
    print("uh oh, x is not less than y") #output: x is less than y

# 3d
if x > y:
    print("how is x greater than y??")
else:
    print("x is NOT greater than y") #output: x is NOT greater than y

# 3e
print("The final value of x is", x, "and the final value of y is", y)
#otuput: The final value of x is 20 and the final value of y is 20