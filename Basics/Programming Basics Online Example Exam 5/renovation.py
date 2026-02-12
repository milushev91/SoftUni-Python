# cook your dish here
from math import ceil

wall_height = int(input())
wall_width = int(input())
not_to_be_paint_percent = int(input()) / 100

paint_used = 0

# calculate surfaces to paint
walls_sq_m = wall_height * wall_width * 4
surfaces_to_paint = ceil(walls_sq_m - walls_sq_m * not_to_be_paint_percent)

# loop until 'Tired!' command is given

command = input()

while command != "Tired!":
    paint_litters = int(command)
    
    paint_used += paint_litters
    
    if paint_used > surfaces_to_paint:
        print(f"All walls are painted and you have {paint_used - surfaces_to_paint} l paint left!")
        break 
    elif paint_used == surfaces_to_paint:
        print("All walls are painted! Great job, Pesho!" )
        break
    command = input()
else:
    print(f"{surfaces_to_paint - paint_used} quadratic m left." )






