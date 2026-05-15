# name game bonus lab

# asking user input
user_name = input("Enter a name: ")

# defining function to create truncated version of song
def trunc_name(name):
    name = name.strip().lower() # making everything lowercase

    if not name: # if name is empty, return empty str
        return ""
    
    vowels = "aeiou"

    if name[0] in vowels: # if starts with vowel, keep as is
        return name
    
    for i, ch in enumerate(name): # otherwise, remove until vowel
        if ch in vowels:
            return name[i:]
        
    return name # if no vowels at all, return name in all lowercase

# testing truncated names
# print(trunc_name("Ann"))
#output: ann

# print(trunc_name("Dan"))
#output: an

# print(trunc_name("Stan"))
#output: an

# generator function for name game
def name_game(name):
    display_name = name.strip().title() # keeping first letter capitalized in display

    base = trunc_name(name) # truncated version of song

    # yielding each line in song
    yield f"{display_name}, {display_name}, bo-b{base}"
    yield f"banana fana fo-f{base}"
    yield f"me my mo-m{base}"
    yield f"{display_name}!"

# testing list of names using user input
test_names = [user_name, "carly",
              "CHARLIE", "Aidan",
              "Braden", "Billy Bob"]

# looping through names and printing
for n in test_names:
    print(f"\nName game for: {n}")
    for line in name_game(n):
        print(line)
#output: Name game for: carly
#        Carly, Carly, bo-barly
#        banana fana fo-farly
#        me my mo-marly
#        Carly!
#
#        Name game for: CHARLIE
#        Charlie, Charlie, bo-barlie
#        banana fana fo-farlie
#        me my mo-marlie
#        Charlie!
#
#        Name game for: Aidan
#        Aidan, Aidan, bo-baidan
#        banana fana fo-faidan
#        me my mo-maidan
#        Aidan!
#
#        Name game for: Braden
#        Braden, Braden, bo-baden
#        banana fana fo-faden
#        me my mo-maden
#        Braden!
#
#        Name game for: Billy Bob
#        Billy Bob, Billy Bob, bo-billy bob
#        banana fana fo-filly bob
#        me my mo-milly bob
#        Billy Bob!

# observations:
# trunc_name function worked for different capitalizations and converted everything to lowercase
# the names that started with a vowel were kept for the names
# names that had one or more consonants were dropping the leading one until there was a vowel in the name
# multi-word names still worked, but truncation only worked on the first vowel in the whole str
# the name_game generator printed yield statements
# only strange result was the multi-word names