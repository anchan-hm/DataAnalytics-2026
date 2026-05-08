# defining a variable (0-23)

# chosen hour (can change whenever)
hour = 2

if 4 <= hour < 10: # 4AM-10AM
    print("Good morning!")
elif 10 <= hour < 17: # 10AM-5PM
    print("Good day!")
elif 17 <= hour < 23: # 5PM-11PM
    print("Good evening!")
elif hour >= 23 or hour < 4: # 11PM-4AM
    print("What are you doing up so late??")

#output: What are you doing up so late??