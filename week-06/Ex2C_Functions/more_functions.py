#defining 3 functions with different paramenters

# creating mailing label with 5 parameters 
def display_mailing_label(name, address, city, state, zip): #defining disaplying_mailing_label
    print(name) #display name
    print(address) #display address
    print(f"{city}, {state} {zip}") #displaying format for mailing label

# adding function to accept any number of arguments, each argument being an integer
def add_numbers(*nums): #defining to allow arguments
    total = sum(nums) #adding all numbers
    numbers_str = " + ".join(str(num) for num in nums) #formatting formula
    print(f"{numbers_str} = {total}") #displaying results

#creating function with two paramenters to comput and display the change due
def display_receipt(total_due, amount_paid): #defining display_recipt
    print(f"Total Due: ${total_due}")
    print(f"Amount Paid: ${amount_paid}")

    if amount_paid > total_due: #overpaid
        change = amount_paid - total_due
        print(f"Change Due: ${change}")

    elif amount_paid == total_due: #exact amount paid
        print("Change Due: $0")
    
    else: #didn't pay enough
        balance = total_due - amount_paid
        print(f"Remaining Balance: ${balance}")

# displaying outputs (testing)
# testing display_mailing_label (1)
display_mailing_label("Alexus Chanthadara", "123 Elevate", "Charlotte", "NC", "12345")
print() #blank line
# testing (2)
display_mailing_label("John Doe", "111 Mystery Ln", "Abyss", "NA", "11111")
print() #blank line
#output: Alexus Chanthadara
#        123 Elevate
#        Charlotte, NC 12345

#        John Doe
#        111 Mystery Ln
#        Abyss, NA 11111

#testing add_numbers (1)
add_numbers(4) #one number
add_numbers(6,10) #two numbers
add_numbers(12,16,18,20) #more than 2 numbers
print()
#output: 4 = 4
#        6 + 10 = 16
#        12 + 16 + 18 + 20 = 66

#testing display_recipt (1)
display_receipt(50,80) #overpaid
print()
#output: Total Due: $50
#        Amount Paid: $80
#        Change Due: $30
#testing (2)
display_receipt(40,40) #exact amount
print()
#output: Total Due: $40
#        Amount Paid: $40
#        Change Due: $0
display_receipt(100,60) #underpaid
print()
#output: Total Due: $100
#        Amount Paid: $60
#        Remaining Balance: $40

#BONUS:
#creating mailing label to use two lines
def display_mailing_label2(name, address1, address2, city, state, zip): #label with 2 addresses
    print(name) #display name
    print(address1) #display first address

    if address2: #print if there is another address
        print(address2) #display second address
    
    print(f"{city}, {state} {zip}") #display rest of mailing label

#testing modification (1)
# two addresses
display_mailing_label2("Alexus Chanthadara", "123 Elevate", "Apt 1A", "Charlotte", "NC", "12345") 
print() #blank line
#output: Alexus Chanthadara
#        123 Elevate
#        Apt 1A
#        Charlotte, NC 12345

#testing modification (2)
# one address
display_mailing_label2("John Doe", "111 Mystery Ln", "", "Abyss", "NA", "11111")
print() #blank line
#output: John Doe
#        111 Mystery Ln
#        Abyss, NA 11111