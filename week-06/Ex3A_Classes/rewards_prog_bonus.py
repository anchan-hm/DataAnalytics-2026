# creating a global list to store customer info
cust_list = [] #empty to be able to run without overwriting existing values

# creating class for RewardsProgram
class RewardsProgram:
    """Customer information for rewards program."""

    def __init__(self, cust_name, phone, email): # creating instance variables
        self.cust_name = cust_name
        self.phone = phone 
        self.email = email

    def profile(self): #method 1
        print(f"Name: {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")

    def thank_you(self): #method 2
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!")

    def add_to_cust_list(self): #method 3
        cust_list.append((self.cust_name, self.phone, self.email)) #adding tuple to global list

# creating customer instances
cust1 = RewardsProgram("Alexus Chanthadara", "111-111-1111", "alexus@email.com")
cust2 = RewardsProgram("John Doe", "222-222-2222", "john@email.com")
cust3 = RewardsProgram("Jane Doe", "333-333-3333", "jane@email.com")
cust4 = RewardsProgram("Dan Daly", "444-444-4444", "dan@email.com")
cust5 = RewardsProgram("Opha May", "555-555-5555", "opha@email.com")

# calling methods
# customer 1
cust1.profile()
cust1.thank_you()
cust1.add_to_cust_list()
#output: Name: Alexus Chanthadara
#        Phone: 111-111-1111
#        Email: alexus@email.com
#        Thank you, Alexus Chanthadara, for visiting our restaurant!

# customer 2
cust2.profile()
cust2.thank_you()
cust2.add_to_cust_list()
#output: Name: John Doe
#        Phone: 222-222-2222
#        Email: john@email.com
#        Thank you, John Doe, for visiting our restaurant!

# customer 3
cust3.profile()
cust3.thank_you()
cust3.add_to_cust_list()
#output: Name: Jane Doe
#        Phone: 333-333-3333
#        Email: jane@email.com
#        Thank you, Jane Doe, for visiting our restaurant!

# customer 4
cust4.profile()
cust4.thank_you()
cust4.add_to_cust_list()
#output: Name: Dan Daly
#        Phone: 444-444-4444
#        Email: dan@email.com
#        Thank you, Dan Daly, for visiting our restaurant!

# customer 5
cust5.profile()
cust5.thank_you()
cust5.add_to_cust_list()
#output: Name: Opha May
#        Phone: 555-555-5555
#        Email: opha@email.com
#        Thank you, Opha May, for visiting our restaurant!

# displaying output
print(cust_list)
#output: [('Alexus Chanthadara', '111-111-1111', 'alexus@email.com'), ('John Doe', '222-222-2222', 'john@email.com'),
#        ('Jane Doe', '333-333-3333', 'jane@email.com'), ('Dan Daly', '444-444-4444', 'dan@email.com'), 
#        ('Opha May', '555-555-5555', 'opha@email.com')]