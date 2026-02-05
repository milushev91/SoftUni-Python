first_player_egss = int(input())
second_player_egss = int(input())

command = input()

while command != "End":
    player = command
    
    if player == "one":
        second_player_egss -= 1 
    else:
        first_player_egss -= 1 
    
    if first_player_egss <= 0:
        print(f"Player one is out of eggs. Player two has {second_player_egss} eggs left.")
        break
    
    if second_player_egss <= 0:
        print(f"Player two is out of eggs. Player one has {first_player_egss} eggs left.")
        break
    
    command = input()
else:
    print(f"Player one has {first_player_egss} eggs left.")
    print(f"Player two has {second_player_egss} eggs left.")
