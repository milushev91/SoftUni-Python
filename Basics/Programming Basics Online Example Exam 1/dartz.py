MULTIPLIER = {
    "Single": 1,
    "Double": 2,
    "Triple": 3,
}

player_name = input()

player_points = 301
successful_shots = unsuccessful_shots = 0

while player_points > 0:
    command = input()

    if command == "Retire":
        print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")
        break
    
    sector = command
    points = int(input()) * MULTIPLIER[sector]

    if points > player_points:
        unsuccessful_shots += 1
        continue
    
    player_points -= points
    successful_shots += 1
else:
    print(f"{player_name} won the leg with {successful_shots} shots.")
