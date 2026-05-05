# calculating tip amount on restaurant bill given the tip percentage (Updated for Lab 3)

# variables
bill = float(input("How much is the restaurant bill? "))
tip_percentage = float(input("What percent tip do you want to leave? ")) 

# tip percentage to decimal
tip_deci = tip_percentage/100

# calculating the tip amount
tip_amount = bill * tip_deci

# displaying the results
print("The tip on a $"+str(bill) + " restaurant bill is $"+format(tip_amount, ".2f"))
# How much is the restaurant bill? 34.50
# What percent tip do you want to leave? 20
# The tip on a $34.5 restaurant bill is $6.9

# pitfalls with input()
# - have to turn it into a float for any math
# - typing letters instead of numbers or else it'll crash
# - not putting anything will cause it to crash