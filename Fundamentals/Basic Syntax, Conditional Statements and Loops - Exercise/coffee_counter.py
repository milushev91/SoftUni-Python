coffees_counter = 0
events = ["coding", "dog", "cat", "movie", "CODING", "DOG", "CAT", "MOVIE"]

command = input()

while command != "END":
    event = command
    
    if event in events:
        if event.isupper():
            coffees_counter += 2
        else:
            coffees_counter += 1 
    
    command = input()

if coffees_counter > 5:
    print("You need extra sleep")
else:
    print(coffees_counter)
