events = input().split("|")
energy = coins = 100

for event in events:
    action, value = event.split("-")
    int_value = int(value)
    
    if action == "rest":
        gained_energy = int_value
        
        if int_value + energy > 100:
            gained_energy = 100 - energy
        
        energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    
    elif action == "order": 
        
        if energy >= 30:
            energy -= 30
            coins += int_value
            print(f"You earned {int_value} coins.")
        else:
            energy += 50
            print("You had to rest!")
    
    else:
        if coins >= int_value:
            coins -= int_value
            print(f"You bought {action}.")
        
        else:
            print(f"Closed! Cannot afford {action}.")
            break 

else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
