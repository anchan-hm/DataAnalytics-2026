# creating variables to test 1
hours_worked = 20
pay_rate = 12.50

if hours_worked > 40:
    overtime = hours_worked - 40
    gross_pay = (40*pay_rate)+(overtime*pay_rate*1.5)
else:
    gross_pay = hours_worked*pay_rate
print("Test 1, Gross Pay is:", gross_pay) #output: Test 1, Gross Pay is: 250.0

# creating variables to test 2
hours_worked2 = 40
pay_rate2 = 25.50

if hours_worked2 > 40:
    overtime2 = hours_worked2 - 40
    gross_pay2 = (40*pay_rate2)+(overtime2*pay_rate2*1.5)
else:
    gross_pay2 = hours_worked2*pay_rate2
print("Test 2, Gross Pay is:", gross_pay2) #Test 2, Gross Pay is: 1020.0

# creating variables to test 3
hours_worked3 = 45
pay_rate3 = 17.30

if hours_worked3 > 40:
    overtime3 = hours_worked3 - 40
    gross_pay3 = (40*pay_rate3)+(overtime3*pay_rate3*1.5)
else:
    gross_pay3 = hours_worked3*pay_rate3
print("Test 3, Gross Pay is:", gross_pay3) #output: Test 3, Gross Pay is: 821.75