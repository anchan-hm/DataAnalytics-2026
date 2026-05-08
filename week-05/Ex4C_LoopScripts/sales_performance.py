# unpacking tuples through loops

# list of tuples
sales_data = [('Marcus Webb', 'East', 4250.00),
              ('Priya Sharma', 'West', 5875.50),
              ('DeShawn Carter', 'East', 3100.75),
              ('LaTonya Rivers', 'South', 6420.00),
              ('Bob Nguyen', 'West', 4980.25),]

#BONUS: adding a variable for total sales
total_sales = 0  #starting at 0

# using loop to unpack EACH tuple
for name, region, sales in sales_data:
    print(f"{name} ({region}): ${sales:,.2f}")
    if sales > 5000:  #adding condition
        print(" ^ Top performer!")
#output: Marcus Webb (East): $4,250.00
#        Priya Sharma (West): $5,875.50
#        ^ Top performer!
#        DeShawn Carter (East): $3,100.75
#        LaTonya Rivers (South): $6,420.00
#        ^ Top performer!
#        Bob Nguyen (West): $4,980.25

    #BONUS: adding to sales
    total_sales += sales #adding after the loop

#BONUS: printing total sales after the loop completion
print("\nTotal sales across all employees: $", format(total_sales, ",.2f")) #using "\n" to start new line
#output: Marcus Webb (East): $4,250.00
#        Priya Sharma (West): $5,875.50
#         ^ Top performer!
#        DeShawn Carter (East): $3,100.75
#        LaTonya Rivers (South): $6,420.00
#         ^ Top performer!
#        Bob Nguyen (West): $4,980.25
#
#        Total sales across all employees: $ 24,626.50