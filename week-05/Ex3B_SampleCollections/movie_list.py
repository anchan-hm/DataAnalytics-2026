# creating a list of movies
fav_movies = ["Iron Man", "Spider Man", "Me Before You"]
watch_list = ["Return To Silent Hill", "Hoppers", "Wake Up Dead Man"]

# using len() to print description
print("The list fav_movies includes my top", len(fav_movies), "favorite movies")
print(fav_movies) #output: The list fav_movies includes my top 3 favorite movies ['Iron Man', 'Spider Man', 'Me Before You']
print("The list watch_list includes the", len(watch_list), "movies I'd like to watch")
print(watch_list) #output: The list watch_list includes the 3 movies I'd like to watch ['Return To Silent Hill', 'Hoppers', 'Wake Up Dead Man']

# using sorted() to organize it A-Z temporarly
print(sorted(fav_movies)) #output: ['Iron Man', 'Me Before You', 'Spider Man']
print(fav_movies) #output: ['Iron Man', 'Spider Man', 'Me Before You']
print(sorted(watch_list)) #output: ['Hoppers', 'Return To Silent Hill', 'Wake Up Dead Man']
print(watch_list)   #output: ['Return To Silent Hill', 'Hoppers', 'Wake Up Dead Man']

# using sort() to organize it A-Z permanately
fav_movies.sort()
print(fav_movies) #output: ['Iron Man', 'Me Before You', 'Spider Man']
watch_list.sort()
print(watch_list) #output: ['Hoppers', 'Return To Silent Hill', 'Wake Up Dead Man']

# using .append() to add to list
fav_movies.append("Avengers")
print("The list fav_movies now includes", len(fav_movies), "movies")
print(fav_movies) #output: The list fav_movies now includes 4 movies ['Iron Man', 'Me Before You', 'Spider Man', 'Avengers']
watch_list.append("Wicked")
print("The list watch_list now includes", len(watch_list), "movies")
print(watch_list) #output: The list watch_list now includes 4 movies ['Hoppers', 'Return To Silent Hill', 'Wake Up Dead Man', 'Wicked']