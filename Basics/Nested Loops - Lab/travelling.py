command = input()

while command != "End":
    destination = command
    budget = float(input())
    
    saved_money = 0
    
    while budget > saved_money:
        amount = float(input())
        saved_money += amount
        
    print(f"Going to {destination}!")
    
    command = input()
