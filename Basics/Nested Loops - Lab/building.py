floors = int(input())
rooms = int(input())

for floor in range(floors, 0, -1):
    letter = ""
    
    if floor == floors:
        letter = "L"
    elif floor % 2 == 0:
        letter = "O"
    else:
        letter = "A"
        
    for room in range(rooms):
        print(f"{letter}{floor}{room}", end=" ")
    print()
