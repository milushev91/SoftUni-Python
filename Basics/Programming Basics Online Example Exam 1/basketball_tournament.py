wins = 0
total_games = 0
command = input()

while command != "End of tournaments":
    tournament_name = command
    games_count = int(input())
    total_games += games_count
    
    for i in range(games_count):
        
        dessi_points = int(input())
        other_team_points = int(input())
        
        difference = abs(dessi_points - other_team_points)
        print(f"Game {i + 1} of tournament {tournament_name}: ", end="")
        
        outcome = ""
        if dessi_points > other_team_points:
            outcome = "win"
            wins += 1
        else:
            outcome = "lost"
       
        print(f"{outcome} with {difference} points.")
    
    command = input()

print(f"{wins / total_games * 100:.2f}% matches win")
print(f"{(total_games - wins) / total_games * 100:.2f}% matches lost")
        
