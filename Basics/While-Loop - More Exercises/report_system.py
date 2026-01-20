needed_amount = int(input())

pay_counter = cash_counter = card_counter = 0
gathered_amount = cash_amount = card_amount = 0

while gathered_amount < needed_amount:
    command = input()
    
    if command == "End":
        print("Failed to collect required money for charity.")
        break
    
    amount = int(command)
    pay_counter +=1 
    
    #cash pay
    if pay_counter % 2 != 0:
        if amount > 100:
            print("Error in transaction!")
            continue
        cash_counter += 1
        cash_amount += amount
        
    #card pay
    else:
        if amount < 10:
            print("Error in transaction!")
            continue
        card_counter += 1
        card_amount += amount
    
    gathered_amount += amount
    print("Product sold!")
    
else:
    print(f"Average CS: {cash_amount / cash_counter:.2f}")
    print(f"Average CC: {card_amount / card_counter:.2f}")
    
    
