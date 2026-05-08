# determining department names based on codes
# USING match/case

# choosing one code to test (can change whenever)
code = 30

match code:
    case 1:
        print("Department:", "Marketing")
    case 5:
        print("Department:", "Human Resources")
    case 10:
        print("Department:", "Accounting")
    case 12:
        print("Department:", "Legal")
    case 18:
        print("Department:", "IT")
    case 20:
        print("Department:", "Customer Relations")
    case _:
        print("No department under this code")

#output: No department under this code