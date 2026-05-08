# determining department names based on codes
#USING if/elif/else

# choosing one code to test (can change whenever)
code = 12

if code == 1:
    print("Department:", "Marketing")
elif code == 5:
    print("Department:", "Human Resources")
elif code == 10:
    print("Department:", "Accounting")
elif code == 12:
    print("Department:", "Legal")
elif code == 18:
    print("Department:", "IT")
elif code == 20:
    print("Department:", "Customer Relations")
else:
    print("No department under this code")

#output: Department: Legal