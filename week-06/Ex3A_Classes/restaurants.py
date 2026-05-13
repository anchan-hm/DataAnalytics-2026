# creating a class for restaurants
class Restaurant:
    """Restaurants and their food type""" #docstring

    def __init__(self, rest_name, food_type): #two instance variables
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self): #method 1 for class
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self): #method 2 for class
        print(f"{self.rest_name} is open.")

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