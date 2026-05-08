# calculating fed tax based on annual gross income and filing status

# using pay_rules to start (can change whenever)
hours_worked = 40
pay_rate = 25.50
filing = "single"  #can change (single or joint)

# calculating WEEKLY gross pay
if hours_worked > 40:
    overtime = hours_worked - 40
    gross_pay = (40*pay_rate)+(overtime*pay_rate*1.5)
else:
    gross_pay = hours_worked*pay_rate

# calculating the ANNUAL gross pay
annual_income = gross_pay*52  # 52 weeks in a year

# tax rate for single filers
if filing == "single":
    if annual_income < 12000:
        tax_rate = 0.05
    elif annual_income < 25000:
        tax_rate = 0.10
    elif annual_income < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20

# tax rate for joint filers
if filing == "joint":
    if annual_income < 12000:
        tax_rate = 0.00
    elif annual_income < 25000:
        tax_rate = 0.06
    elif annual_income < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20

# calculating weekly tax
weekly_tax = gross_pay*tax_rate

# calculating net pay
net_pay = gross_pay-weekly_tax

# print outputs
print("You worked", hours_worked, "hours this period.")
print("Because you earn $", pay_rate, "per hour, your gross weekly pay is $", round(gross_pay, 2))
print("Your filing status is:", filing)
print("Your tax withholding for the week is $", round(weekly_tax, 2))
print("Your net pay is $", round(net_pay, 2))

#output:
# You worked 40 hours this period.
# Because you earn $ 25.5 per hour, your gross weekly pay is $ 1020.0
# Your filing status is: single
# Your tax withholding for the week is $ 153.0
# Your net pay is $ 867.0