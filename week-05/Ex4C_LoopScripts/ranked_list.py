#  creating a ranking list for loop

# creating a list
fav_food = ["sushi", "katsu curry", "beef bowl", "miso soup", "pho", "papaya salad"]

# using enumerate() with "for" loop for numbering
for index, item in enumerate(fav_food, start=1):  #starting at 1
    if index == 1:
        print(index, ".", item, "<- top pick!") #adding "." after number and top pick for the number 1
    else:
        print(index, ".", item) #adding "." after number
#output: 1 . sushi <- top pick!
#        2 . katsu curry
#        3 . beef bowl
#        4 . miso soup
#        5 . pho
#        6 . papaya salad

# BONUS: reverse order
print("\nReversed order:") # "\n" to start a new line (added space between lists)
for index, item in enumerate(reversed(fav_food), start=1):
    print(index, ".", item)
#output: Reversed order:
#        1 . papaya salad
#        2 . pho
#        3 . miso soup
#        4 . beef bowl
#        5 . katsu curry
#        6 . sushi