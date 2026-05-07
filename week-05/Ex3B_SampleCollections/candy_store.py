# creating tuples
candy_types = ("hard candy", "gummies", "taffy")
flavors = ("strawberry", "watermelon", "blueberry")

## making a set for candy combinations
combos = set()

combos.add(candy_types[0]+"-"+flavors[1])
combos.add(candy_types[1]+"-"+flavors[2])
combos.add(candy_types[2]+"-"+flavors[0])

# printing candy options
print("Today's candy options include:")
print(combos) #output: Today's candy options include: {'gummies-blueberry', 'hard candy-watermelon', 'taffy-strawberry'}

# printing to observe combos
print(combos) #output: Today's candy options include: {'gummies-blueberry', 'taffy-strawberry', 'hard candy-watermelon'}
print(combos) #output: Today's candy options include: {'taffy-strawberry', 'gummies-blueberry', 'hard candy-watermelon'}
print(combos) #output: Today's candy options include: {'hard candy-watermelon', 'gummies-blueberry', 'taffy-strawberry'}