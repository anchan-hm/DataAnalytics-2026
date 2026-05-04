# **Lab 1**
# variables with snake_case
customer_id = "Customer ID"
customer_name = "Customer's Name"
customer_gender = "Customer Gender"
date_of_birth = "Customer date of birth"
license_number = "Driver's License Number"
policy_number = "Auto Policy Number"

# assumptions
customer_id = 1004
# could not start with 0 and add more after because it changed the value
customer_name = "Alexus Chanthadara"
# used plain first and last name to keep it simple
customer_gender = "Female"
# made sure to align the gender to person
date_of_birth = '04-20-1998'
# added date as string
license_number = 1123456789
# could not start with 0 because it would change the value after
policy_number = 1004

# printing to make sure the output is correct
print(customer_name)
print(customer_gender)
print(customer_id)
print(date_of_birth)
print(license_number)
print(policy_number)

# my variables
my_name = "Alexus Chanthadara"
birth_city = "Asheboro"

# printing to make sure the output is correct
print(my_name + " " + birth_city)


# **Lab 2**
#a) What is the full list of reserved words that can’t be used for variable names?

# listed below
import keyword
print(keyword.kwlist)
#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
# 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

print(len(keyword.kwlist))
# 35 count


#b) Pick 5 of these words and review the explanation for how it is used as a keyword in
#Python. Add these 5 definitions as # comments to your exercise document. Put ^^
#around any terms that you are not familiar with.

# keyword: ^^assert^^
# assert is used for debugging
# ex:
def divide(a, b):
    assert b != 0, "Divisor cannot be zero."
    return a / b

divide (5, 0)
# output: Divisor cannot be zero

# keyword: ^^nonlocal^^
# nonlocal is used in functions inside functions to create anonymous functions
# ex:
def outer():
  x = "Welcome"
  def inner():
    nonlocal x
    x = "to Flexiple"
  inner() 
  return x
print(outer())
# output: to Flexible

# keyword: ^^global^^
# accessing a global variable is simple as any other variable but to modify a global variable, you need to use the global keyword
# ex:
age = 18
def check():
       global age
       age = 16

check()
print (age)
# output: 16
# The age variable is a global variable and we cannot change it's value without using the global statement.

# keyword: ^^raise^^
# used to raise an error. These errors are visible in the traceback and they cancel the execution of the program is not handled properly
# ex:
enter = "nick"
if not type(enter) is int:
       raise TypeError("Only integers are allowed.")
# output: TypeError: Only integers are allowed
# TypeError is raised if the variable does not contain integers.

# keyword: break
# is a control flow statement used to come out of a loop
# ex: 
age = 19
if age >= 18:
       print ("You are eligible to vote.")
       break
# output: You are eligible to vote.
# As soon as the condition is satisfied, the break statement ends the loop.