# rule of 72 (doubling)

# example values
savings = 8000
interest_rate = 0.05 # 5% interest rate

# calculating years to double
years_double = 72/(interest_rate*100)

# calculating doubled value
doubled_value = savings*2

# displaying the results
print("Your current savings is $" + str(savings) + ".")
print("At a " + format(interest_rate, ".0%") + " interest rate, your savings account will be")
print("worth $" + format(doubled_value, ".2f") + " in " + format(years_double, ".1f") + " years")
# Your current savings is $8000.
# At a 5% interest rate, your savings account will be
# worth $16000.00 in 14.4 years