clients_count = int(input())

product_prices = {
    "basket": 1.50,
    "wreath": 3.80,
    "chocolate bunny": 7,
}

income = 0

for _ in range(clients_count):
    
    command = input()
    bill = 0
    items_count = 0
    
    while command != "Finish":
        item = command
        bill += product_prices[item]
        items_count += 1
        command = input()
    
    if items_count % 2 == 0:
        bill *= 0.80
    
    print(f"You purchased {items_count} items for {bill:.2f} leva.")
    income += bill

print(f"Average bill per client is: {income / clients_count:.2f} leva.")
