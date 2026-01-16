tour_price = float(input())
budget = float(input())

spend_days = 0
days_counter = 0

while budget < tour_price:
    activity = input()
    amount = float(input())
    
    days_counter += 1
    
    if activity == "spend":
        spend_days += 1 
        budget -= amount
        
        if budget < 0:
            budget = 0
        
        if spend_days == 5:
            print("You can't save the money.")
            print(days_counter)
            break
    else:
        spend_days = 0
        budget += amount
else:
    print(f"You saved the money for {days_counter} days.")
        
    
    
