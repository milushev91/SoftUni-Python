# cook your dish here
MAX_PRICES = {
    "Clothes": 50.00,
    "Shoes": 35.00,
    "Accessories": 20.50,
    }
TICKET_PRICE = 150
    
products_line = input().split("|")
budget = float(input())
profit = 0
profits = []

for product_line in products_line:
    name, price = product_line.split("->")
    float_price = float(price)
    max_price = MAX_PRICES[name]
    
    if float_price > max_price or float_price > budget:
        continue
    
    up_percent = float_price * 0.40
    profit += up_percent
    profits.append(f"{float_price + up_percent:.2f}")
    budget -= float_price
    
print(*profits, sep=" ")
print(f"Profit: {profit:.2f}")

total_money = sum(float(price) for price in profits) + budget

if total_money >= TICKET_PRICE:
    print("Hello, France!")
else:
    print("Not enough money.")
