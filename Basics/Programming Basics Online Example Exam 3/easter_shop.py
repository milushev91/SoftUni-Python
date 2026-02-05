eggs_count = int(input())

sold_eggs = 0
command = input()

while command != "Close":
    action = command
    quantity = int(input())
    
    if action == "Buy":
        
        if quantity > eggs_count:
            print("Not enough eggs in store!")
            print(f"You can buy only {eggs_count}.")
            break
        eggs_count -= quantity
        sold_eggs += quantity
        
    else:
        eggs_count += quantity

    command = input()
else:
    print("Store is closed!")
    print(f"{sold_eggs} eggs sold.")

    
    
