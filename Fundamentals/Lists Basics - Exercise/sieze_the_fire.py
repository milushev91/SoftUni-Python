# cook your dish here
#High = 89#Low = 28#Medium = 77#Low = 23

cells = input().split("#")
water = int(input())

effort = 0
total_fire = 0

print("Cells:")

for cell in cells:
    ftype, value = cell.split(" = ")
    int_value = int(value)
    
    if ftype == "Low":
        if int_value < 1 or int_value > 50:
            continue
    elif ftype == "Medium":
        if int_value < 51 or int_value > 80:
            continue
    else:
        if int_value < 81 or int_value > 125:
            continue
    
    if int_value > water:
        continue
    
    print(f" - {int_value}")
    
    water -= int_value
    effort += int_value * 0.25 
    total_fire += int_value
    
    if int_value <= 0:
        break

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
