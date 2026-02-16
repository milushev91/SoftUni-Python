best_player = ""
best_player_goals = 0

command = input()

while command != "END":
    player_name = command
    player_goals = int(input())
    
    if player_goals > best_player_goals:
        best_player_goals = player_goals
        best_player = player_name
    
    if player_goals >= 10:
        break
    
    command = input()

print(f"{best_player} is the best player!")

if player_goals >= 3:
    print(f"He has scored {best_player_goals} goals and made a hat-trick !!!")
else: 
    print(f"He has scored {player_goals} goals.")

