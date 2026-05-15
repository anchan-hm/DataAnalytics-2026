# open the file in read mode
f = open("about_me.txt", "r")

# print file in terminal
print(f.read())
#output:Name: Alexus
#       Place of birth: North Carolina
#       Pets growing up: dogs
#       Travel to for ONE WEEK: Greece
#       Live at for a YEAR: Japan
#       If I could have the perfect night out, I would go to my favorite boba and eat some onigiri.

# close file
f.close()