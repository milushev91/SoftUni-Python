easter_breads_count = int(input())
max_points = 0
max_points_name = None

for _ in range(easter_breads_count):
    name = input()
    
    command = input()
    points = 0
    
    while command != "Stop":
        points += int(command)
        command = input()
    
    print(f"{name} has {points} points.")
    
    if points > max_points:
        max_points = points 
        max_points_name = name 
        print(f"{name} is the new number 1!")

print(f"{max_points_name} won competition with {max_points} points!")

    
    
