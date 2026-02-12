player_stats = {}

command = input()
winner = 0 
max_points = 0

while command != "Stop":
    name = command
    player_points = 0
   
    for letter in name:
        num = int(input())
        points = 2
        
        if ord(letter) == num:
            points = 10 
        
        player_points += points
    
    if player_points >= max_points:
        max_points = player_points
        winner = name
        
    command = input()

print(f"The winner is {winner} with {max_points} points!")
