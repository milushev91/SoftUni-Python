orders_count = int(input())
income = 0

for _ in range(orders_count):
    
    capsule_price = float(input())
    days = int(input())
    capsules_per_day = int(input())
    
    if capsule_price < 0.01 or capsule_price > 100:
        continue
    
    if days < 1 or days > 31:
        continue
    
    if capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    
    order_bill = capsules_per_day * capsule_price * days
    
    print(f"The price for the coffee is: ${order_bill:.2f}")
    
    income += order_bill
    
print(f"Total: ${income:.2f}")
