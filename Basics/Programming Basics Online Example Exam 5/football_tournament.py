# cook your dish here
POINTS = {
    "W": 3,
    "D": 1,
    "L": 0,
}

football_team = input()
matches_count = int(input())

if matches_count == 0:
    print(f"{football_team} hasn't played any games during this season.")
else:
    football_team_stats = {
        "W": 0,
        "D": 0,
        "L": 0,  
    }
    
    points_won = 0
    
    for _ in range(matches_count):
        outcome = input()
        points = POINTS[outcome]
        points_won += points
        football_team_stats[outcome] += 1
    
    print(f"{football_team} has won {points_won} points during this season.")
    print("Total stats:")
    
    for key, value in football_team_stats.items():
        print(f"## {key}: {value}")
    
    print(f"Win rate: {football_team_stats['W'] / matches_count * 100:.2f}%")
