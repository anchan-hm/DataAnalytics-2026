# Testing years to see if they are leap year

# Test 1
year = 1900
# USING 400, 100, 4 for Gregorian leap year rules
if year % 400 == 0: # using % to find the remainder
    print("Test 1:", year, "is a leap year")
elif year % 100 == 0:
    print("Test 1:", year, "is NOT a leap year")
elif year % 4 == 0:
    print("Test 1:", year, "is a leap year")
else:
    print("Test 1:", year, "is NOT a leap year")
#output: Test 1: 1900 is NOT a leap year

# Test 2
year2 = 1950

if year2 % 400 == 0:
    print("Test 2:", year2, "is a leap year")
elif year2 % 100 == 0:
    print("Test 2:", year2, "is NOT a leap year")
elif year2 % 4 == 0:
    print("Test 2:", year2, "is a leap year")
else:
    print("Test 2:", year2, "is NOT a leap year")
#output: Test 2: 1950 is NOT a leap year

# Test 3
year3 = 1999

if year3 % 400 == 0:
    print("Test 3:", year3, "is a leap year")
elif year3 % 100 == 0:
    print("Test 3:", year3, "is NOT a leap year")
elif year3 % 4 == 0:
    print("Test 3:", year3, "is a leap year")
else:
    print("Test 3:", year3, "is NOT a leap year")
#output: Test 3: 1999 is NOT a leap year

# Test 4
year4 = 2000

if year4 % 400 == 0:
    print("Test 4:", year4, "is a leap year")
elif year4 % 100 == 0:
    print("Test 4:", year4, "is NOT a leap year")
elif year4 % 4 == 0:
    print("Test 4:", year4, "is a leap year")
else:
    print("Test 4:", year4, "is NOT a leap year")
#output: Test 4: 2000 is a leap year

# Test 5
year5 = 2001

if year5 % 400 == 0:
    print("Test 5:", year5, "is a leap year")
elif year5 % 100 == 0:
    print("Test 5:", year5, "is NOT a leap year")
elif year5 % 4 == 0:
    print("Test 5:", year5, "is a leap year")
else:
    print("Test 5:", year5, "is NOT a leap year")
#output: Test 5: 2001 is NOT a leap year

# Test 6
year6 = 20212

if year6 % 400 == 0:
    print("Test 6:", year6, "is a leap year")
elif year6 % 100 == 0:
    print("Test 6:", year6, "is NOT a leap year")
elif year6 % 4 == 0:
    print("Test 6:", year6, "is a leap year")
else:
    print("Test 6:", year6, "is NOT a leap year")
#output: Test 6: 20212 is a leap year