# cook your dish here
voucher_amount = int(input())

bought_tickets_count = bought_others_count = 0

command = input()

while command != "End":
    item = command
    end = 1
    
    if len(item) > 8:
        end = 2
        bought_tickets_count += 1 
    else:
        bought_others_count += 1 
 
    price = sum(ord(char) for char in item[:end])
    
    if price > voucher_amount:
        if end == 2:
            bought_tickets_count -= 1
        else:
            bought_others_count -= 1
        break 
    
    voucher_amount -= price
    
    command = input()
    
print(bought_tickets_count)
print(bought_others_count)
