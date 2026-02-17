budget = float(input())

products_sold = 0
spent_money = 0
product_counter = 0

command = input()

while command != "Stop":
    product_name = command
    product_price = float(input())
    
    product_counter += 1 
    
    if product_counter % 3 == 0:
        product_price /= 2
    
    if product_price > budget:
        print("You don't have enough money!")
        print(f"You need {product_price - budget:.2f} leva!")
        break
    else:
        products_sold += 1 
        budget -= product_price
        spent_money += product_price
    
    command = input()
else:
    print(f"You bought {products_sold} products for {spent_money:.2f} leva.")
