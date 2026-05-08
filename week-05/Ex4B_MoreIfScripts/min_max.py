# displaying both the smallest AND the largest of the three

#creating variables (can change whenever)
a = 45
b = 42
c = 46

# finding the smallest
if a < b and a < c:
    smallest = a
elif b < a and b < c:
    smallest = b
else:
    smallest = c

# finding the largest
if a > b and a > c:
    largest = a
elif b > a and b > c:
    largest = b
else:
    largest = c

# displaying outputs
print("The smallest out of the three is:", smallest)
print("The largest out of the three is:", largest)
#output: The smallest out of the three is: 42
#        The largest out of the three is: 46