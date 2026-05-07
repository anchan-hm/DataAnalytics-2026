# data cleaning

# variables
name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,500"

# using .lower() for names
print(name_1.lower()) #output: priya sharma
print(name_2.lower()) #output: bob nguyen
print(name_3.lower()) #output: latonya williams

# using .title() to capitalize first letter of names
print(name_1.title())  #output: Priya Sharma
print(name_2.title())  #output: Bob Nguyen
print(name_3.title())  #output: Latonya Williams

# using .replace() to remove $
salary_1_new = salary_1.replace("$","")
salary_2_new = salary_2.replace("$","")
print(salary_1_new)  #output: 82,500
print(salary_2_new)  #output: 74,500

# checking data
print(type(salary_1_new))  #output: <class 'str'>
print(type(salary_2_new))  #output: <class 'str'>

# next step to perform math
salary_1_int = int(salary_1.replace("$","").replace(",","")) #taking out comma
print(salary_1_int)  #output: 82500
print(type(salary_1_int))  #output: <class 'int'>