first_player_name = input()
second_player_name = input()

first_player_points = 0
second_player_points = 0

command = input()

while command != "End of game":
    first_player_card = int(command)
    second_player_card = int(input())
    
    difference = abs(first_player_card - second_player_card)
    
    if first_player_card > second_player_card:
        first_player_points += difference
    elif second_player_card > first_player_card:
        second_player_points += difference
    else:
        first_player_card = int(input())
        second_player_card = int(input())
        
        winner = ""
        points = 0
        print("Number wars!")
        
        if first_player_card > second_player_card:
            winner = first_player_name
            points += first_player_points
        else:
            winner = second_player_name
            points += second_player_points
        
        print(f"{winner} is winner with {points} points")
        break
    command = input()
else:
    print(f"{first_player_name} has {first_player_points} points")
    print(f"{second_player_name} has {second_player_points} points")
            
            
