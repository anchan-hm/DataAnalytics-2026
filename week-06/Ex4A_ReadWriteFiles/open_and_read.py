# open the file in read mode
f = open("about_me.txt", "r")

# print file in terminal
# print(f.read())
#output:Name: Alexus
#       Place of birth: North Carolina
#       Pets growing up: dogs
#       Travel to for ONE WEEK: Greece
#       Live at for a YEAR: Japan
#       If I could have the perfect night out, I would go to my favorite boba and eat some onigiri.

# printing parts
# print(f.read(50)) # first 50 characters
# print(f.read(50)) # next 50 characters
#output: Name: Alexus
#        Place of birth: North Carolina
#        Pets g
#        rowing up: dogs
#        Travel to for ONE WEEK: Greece
#        Liv

# printing even more parts
# print(f.readline(10)) # first 10 of first line
# print(f.readline()) # reads the rest of that line
#
# for i in range(1,5): #looping
#     print(f.readline()) # reading the next 4 lines
#output: Name: Alex
#        us
#
#        Place of birth: North Carolina
#
#        Pets growing up: dogs
#
#        Travel to for ONE WEEK: Greece
#
#        Live at for a YEAR: Japan

# using readlines()
# a) print(f.readlines(1)) # reading parts of the first line
#output: ['Name: Alexus\n']

# b) print(f.readlines(1)) # continuing
#output: ['Name: Alexus\n']
#        ['Place of birth: North Carolina\n']

# c) print(f.readlines(10)) # reading more
#output: ['Name: Alexus\n']
#        ['Place of birth: North Carolina\n']
#        ['Pets growing up: dogs\n']

# d) print(f.readlines(10)) # continues reading
#output: ['Name: Alexus\n']
#        ['Place of birth: North Carolina\n']
#        ['Pets growing up: dogs\n']
#        ['Travel to for ONE WEEK: Greece\n']

# e1) print(f.readlines(100)) # reading a larger amount
#output: ['Name: Alexus\n']
#        ['Place of birth: North Carolina\n']
#        ['Pets growing up: dogs\n']
#        ['Travel to for ONE WEEK: Greece\n']
#        ['Live at for a YEAR: Japan\n', 'If I could have the perfect night out, I would go to my favorite boba and eat some onigiri.\n']

# e2) print(f.readlines(-1)) # finish reading the file
#output: ['Name: Alexus\n']
#        ['Place of birth: North Carolina\n']
#        ['Pets growing up: dogs\n']
#        ['Travel to for ONE WEEK: Greece\n']
#        ['Live at for a YEAR: Japan\n', 'If I could have the perfect night out, I would go to my favorite boba and eat some onigiri.\n']
#        []

# trying a new combination of read methods
# a) first 50 characters
first_50 = f.read(50)

# b) next 4 lines being stored as list
next_lines = []
for i in range(4):
    next_lines.append(f.readline())

# c) read next 100 characters
next_100 = f.readlines(100)

# displaying output
print("First 50 characters:", first_50)
print("Next 4 lines, as list:", next_lines)
print("Next 100 characters:", next_100)
#output: First 50 characters: Name: Alexus
#        Place of birth: North Carolina
#        Pets g
#        Next 4 lines, as list: ['rowing up: dogs\n', 'Travel to for ONE WEEK: Greece\n', 'Live at for a YEAR: Japan\n', 'If I could have the perfect night out, I would go to my favorite boba and eat some onigiri.\n']
#        Next 100 characters: []

# close file
f.close()