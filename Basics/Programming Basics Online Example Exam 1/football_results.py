MATCHES_COUNT = 3

wins = loses = draws = 0

matches = [input() for _ in range(MATCHES_COUNT)]


for match in matches:
    score1, score2 = [int(score) for score in match.split(":")]
    
    if score1 > score2:
        wins += 1 
    elif score1 < score2:
        loses += 1 
    else:
        draws += 1
    
print(f"Team won {wins} games.")
print(f"Team lost {loses} games.")
print(f"Drawn games: {draws}")
