# monthly salary taxed 23% for Fed taxes

salary = 4311 # example for monthly salary
fed_tax = 0.23 # federal taxes
after_tax = salary*fed_tax #result after taxes are taken out
rounding_taxes = round(after_tax, 2) # try using round()

# displaying results
print(f"Federal taxes taken out: ${after_tax:.2f}")
# Federal taxes taken out: $991.53