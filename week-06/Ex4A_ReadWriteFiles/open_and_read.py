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
print(f.readline(10)) # first 10 of first line
print(f.readline()) # reads the rest of that line

for i in range(1,5): #looping
    print(f.readline()) # reading the next 4 lines
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

# close file
f.close()