# cook your dish here
LIMIT = 7

best_movie = ""
points = 0

for _ in range(7):
    command = input()
    
    if command == "STOP":
        break
    
    movie_name = command
    movie_name_length = len(movie_name)
    ascii_sum = 0
    
    for char in movie_name:
        ascii_sum += ord(char)
        if char.islower():
            ascii_sum -= 2 * movie_name_length
        elif char.isupper():
            ascii_sum -= movie_name_length
    
    if ascii_sum > points:
        points = ascii_sum
        best_movie = movie_name
  
else:
    print("The limit is reached.")

print(f"The best movie for you is {best_movie} with {points} ASCII sum.")
