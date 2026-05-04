customer_id = "Customer ID"
customer_name = "Customer's Name"
customer_gender = "Customer Gender"
date_of_birth = "Customer date of birth"
license_number = "Driver's License Number"
policy_number = "Auto Policy Number"

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

print(customer_name)
print(customer_gender)
print(customer_id)
print(date_of_birth)
print(license_number)
print(policy_number)

my_name = "Alexus Chanthadara"
birth_city = "Asheboro"

print(my_name + " " + birth_city)


#a) What is the full list of reserved words that can’t be used for variable names?
# listed below
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))


#b) Pick 5 of these words and review the explanation for how it is used as a keyword in
#Python. Add these 5 definitions as # comments to your exercise document. Put ^^
#around any terms that you are not familiar with.