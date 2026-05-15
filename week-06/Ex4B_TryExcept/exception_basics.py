# ValueError
try:
    num = int("hello") # trying to convert string into int
except ValueError:
    print("ValueError: Oops, looks like you tried to turn a string into a integer.")
else:
    print(num)
finally:
    print("Let's try another one...\n")
#output: ValueError: Oops, looks like you tried to turn a string into a integer.
#        Let's try another one...

# NameError
try:
    result = banana # banana not defined
except NameError:
    print("NameError: Oops, looks like you tried to use a variable that isn't defined.")
else:
    print(result)
finally:
    print("Let's try another one...\n")
#output: NameError: Oops, looks like you tried to use a variable that isn't defined.
#        Let's try another one...

# TypeError
try:
    total = "5" + 10 # cannot add string to integer
except TypeError:
    print("TypeError: Oops, looks like you tried to add different data types.")
else:
    print(total)
finally:
    print("Let's try another one...\n")
#output: TypeError: Oops, looks like you tried to add different data types.
#        Let's try another one...

# SyntaxError
try:
    eval("x === 5") # Python code is invalid
except SyntaxError:
    print("SyntaxError: Oops, looks like you tried to enter an invalid Python code.")
else:
    print("No SyntaxError found.")
finally:
    print("Let's try another one...\n")
#output: SyntaxError: Oops, looks like you tried to enter an invalid Python code.
#        Let's try another one...