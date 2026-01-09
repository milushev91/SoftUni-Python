tournaments_count = int(input())
start_points = int(input())

stages_points ={
    "W": 2000,
    "F": 1200,
    "SF": 720,
}

won_points = 0
wins = average_points = 0 

for _ in range(tournaments_count):
    stage = input()
    
    won_points += stages_points[stage]
    
    if stage == "W":
        wins += 1 

print(f"Final points: {won_points + start_points}")
print(f"Average points: {int(won_points / tournaments_count)}")
print(f"{wins / tournaments_count * 100:.2f}%")
    
