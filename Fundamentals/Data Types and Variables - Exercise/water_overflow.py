TANK_CAPACITY = 255

n = int(input())
tank_lv = 0

for _ in range(n):
    litters = int(input())
    
    if litters + tank_lv > TANK_CAPACITY:
        print("Insufficient capacity!")
        continue
    
    tank_lv += litters

print(tank_lv)
