# creating variable to use open function

# creating about_me.txt and adding
f = open("about_me.txt", "a") # adding file if missing

# adding perfect night out
f.write("\nIf I could have the perfect night out, I would go to my favorite boba and eat some onigiri.\n")

f.close() # closing file once created
#output: Name: Alexus
#        Place of birth: North Carolina
#        Pets growing up: dogs
#        Travel to for ONE WEEK: Greece
#        Live at for a YEAR: Japan
#        If I could have the perfect night out, I would go to my favorite boba and eat some onigiri.
