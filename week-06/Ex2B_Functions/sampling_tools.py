#importing random library
import random

#adding product inventory
products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
            'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp',
            'Surge Protector']

#scenario a-b
# a) "Product of the Day"
product_of_day = random.choice(products) #using random.choice to select product randomly
print("Product of the Day:", product_of_day) #displaying product of the day with random product each time
#output: 1) Product of the Day: Headset
#        2) Product of the Day: Desk Lamp
#        3) Product of the Day: Docking Station

# b) 3 products for usability survey (no repeats)
product_survey = random.sample(products, 3) #selecting 3 products at random (no repeats)
print("Usability Survey Products:", product_survey) #displaying 3 different products at random
#output: 1) Product of the Day: Headset
#        Usability Survey Products: ['USB Hub', 'Mouse', 'Laptop']
#        2) Product of the Day: Surge Protector
#        Usability Survey Products: ['Docking Station', 'Keyboard', 'Desk Lamp']
#        3) Product of the Day: Laptop
#        Usability Survey Products: ['Surge Protector', 'Mouse', 'Webcam']

# c) randomizing product order (no ranking)
random.shuffle(products) #shuffling list of products
print("Shuffle Product List:", products) #disaplying results for list
#output: 1) Shuffle Product List: ['Docking Station', 'Surge Protector', 'Mouse', 'Monitor', 'USB Hub', 'Keyboard', 
#        'Desk Lamp', 'Laptop', 'Webcam', 'Headset']
#        2) Shuffle Product List: ['Desk Lamp', 'Surge Protector', 'Laptop', 'USB Hub', 'Monitor', 'Keyboard', 
#        'Docking Station', 'Headset', 'Mouse', 'Webcam']
#        3) Shuffle Product List: ['Laptop', 'Mouse', 'Monitor', 'Desk Lamp', 'Webcam', 'Docking Station', 
#        'Surge Protector', 'USB Hub', 'Keyboard', 'Headset']

# d) generating a simulated daily transaction count (50-300)
transactions = random.randint(50, 300) #picking count between 50 and 300
print("Daily Transaction Count:", transactions) #displaying results
#output: 1) Daily Transaction Count: 275
#        2) Daily Transaction Count: 99
#        3) Daily Transaction Count: 246