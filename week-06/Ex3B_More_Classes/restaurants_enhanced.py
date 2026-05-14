# enhancing previous class for restaurants to add tracking and ratings
class Restaurant:
    """Restaurants and their food type, customers served and rating""" # docstring

    def __init__(self, rest_name, food_type): # two instance variables
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0 # default attribute
        self.customer_ratings = [] # default attribute (empty list)

    def describe_rest(self): # method 1 for class
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self): # method 2 for class
        print(f"{self.rest_name} is open.")

    def add_num_served(self): # new method being added (3)
        """Asking how many customers were served today and total.""" # docstring
        try:
            num = int(input("How many customers served today?")) # creating user input
            if num < 0: # making sure input is valid (above 0)
                print("Number cannot be negative.")
                return # ensuring to keep info without updating
            self.number_served += num # add to total served
        except ValueError: # ensuring input is valid
            print("Please enter valid whole number.")

    def print_num_served(self): # new method being added (4)
        print(f"{self.rest_name} has served {self.number_served} customers.") # displaying output

    def customer_rating(self): # new method being added (5)
        """What rating would you give, valid user input, updating list, displaying average.""" # docstring
        while True: # loop till valid input
            rating = input("Rate your experience (1-5): ") # user input for rating

            #input
            if rating.isdigit(): # checking value
                rating = int(rating) # making sure it is a integar
                if 1 <= rating <= 5: # rating 1-5
                    self.customer_ratings.append(rating) # adding rating for store
                    avg = sum(self.customer_ratings)/len(self.customer_ratings) # average of overall rating
                    print(f"Your rating was {rating}. The average rating is {avg:.2f}.") # displaying output
                    break #breaking loop
                else:
                    print("Rating must be between 1 & 5.") # a whole number (1-5)
            else:
                print("Enter a whole number between 1 & 5.") # a whole number

# creating 3 instances of class for different types of restaurant
# using workbook examples
rest1 = Restaurant("Burber Kirg", "burgers")
rest2 = Restaurant("Taco Baco", "tacos")
rest3 = Restaurant("A&A", "AAAAAAAAA")

# calling instances
rest1.describe_rest()
rest1.rest_open()
#output: Burber Kirg serves burgers.
#        Burber Kirg is open.

rest2.describe_rest()
rest2.rest_open()
#output: Taco Baco serves tacos.
#        Taco Baco is open.

rest3.describe_rest()
rest3.rest_open()
#output: A&A serves AAAAAAAAA.
#        A&A is open.

# testing customer served & rating modifications

# restaurant 1
# number served
rest1.print_num_served()
rest1.add_num_served()
rest1.add_num_served()
rest1.print_num_served()
#output: Burber Kirg has served 0 customers.
#        How many customers served today?20
#        How many customers served today?10
#        Burber Kirg has served 30 customers.

# ratings
rest1.customer_rating()
rest1.customer_rating()
rest1.customer_rating()
#output: Rate your experience (1-5): 3
#        Your rating was 3. The average rating is 3.00.
#        Rate your experience (1-5): 5
#        Your rating was 5. The average rating is 4.00.
#        Rate your experience (1-5): 2
#        Your rating was 2. The average rating is 3.33.

# restaurant 2
# number served
rest2.print_num_served()
rest2.add_num_served()
rest2.add_num_served()
rest2.print_num_served()
#output: Taco Baco has served 0 customers.
#        How many customers served today?10
#        How many customers served today?20
#        Taco Baco has served 30 customers.

# ratings
rest2.customer_rating()
rest2.customer_rating()
rest2.customer_rating()
#output: Rate your experience (1-5): 1
#        Your rating was 1. The average rating is 1.00.
#        Rate your experience (1-5): 5
#        Your rating was 5. The average rating is 3.00.
#        Rate your experience (1-5): 1
#        Your rating was 1. The average rating is 2.33.

# restaurant 3
# number served
rest3.print_num_served()
rest3.add_num_served()
rest3.add_num_served()
rest3.print_num_served()
#output: A&A has served 0 customers.
#        How many customers served today?5
#        How many customers served today?2
#        A&A has served 7 customers.

# ratings
rest3.customer_rating()
rest3.customer_rating()
rest3.customer_rating()
#output: Rate your experience (1-5): 2
#        Your rating was 2. The average rating is 2.00.
#        Rate your experience (1-5): 2
#        Your rating was 2. The average rating is 2.00.
#        Rate your experience (1-5): 2
#        Your rating was 2. The average rating is 2.00.