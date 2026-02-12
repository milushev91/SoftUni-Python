games_count = int(input())

games_statistic = {
    "Hearthstone": 0,
    "Fornite": 0,
    "Overwatch": 0
}
other_games = 0

for _ in range(games_count):
    game = input()
    
    if game in games_statistic:
        games_statistic[game] += 1
    else:
        other_games += 1

for key, value in games_statistic.items():
    print(f"{key} - {value / games_count * 100:.2f}%")
print(f"Others - {other_games / games_count * 100:.2f}%")
