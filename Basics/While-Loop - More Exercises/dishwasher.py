detergent_bottles = int(input())

detergent_mls = detergent_bottles * 750
dish_number = 0
washed_plates = washed_pots = 0

command = input()

while command != "End":
    dishes = int(command)
    dish_number += 1
    used_detergent = 5
    
    if dish_number % 3 == 0:
        used_detergent = 15
        washed_pots += dishes
    else:
        washed_plates += dishes
    
    used_detergent *= dishes
    detergent_mls -= used_detergent
    
    if detergent_mls < 0:
        print(f"Not enough detergent, {abs(detergent_mls)} ml. more necessary!")
        break
    
    command = input()
else:
    print("Detergent was enough!")
    print(f"{washed_plates} dishes and {washed_pots} pots were washed.")
    print(f"Leftover detergent {detergent_mls} ml.")
    
    
