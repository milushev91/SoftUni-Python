cards = input().split()

teams = {
    "A": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"],
    "B": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"],
}

game_terminated = False

for card in cards:
    team, number = card.split("-")
    team_players = teams[team]
    
    if number not in team_players:
        continue
    
    team_players.remove(number)
    
    if len(team_players) < 7:
        game_terminated = True
        break

for team, players in teams.items():
    line = f"Team {team} - {len(players)}"
    seperator ="; "
    
    if team == "B":
        seperator = "\n"
    
    print(line, end=seperator)

if game_terminated:
    print("Game was terminated")
