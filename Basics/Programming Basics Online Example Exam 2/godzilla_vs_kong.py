# cook your dish here
budget = float(input())
statists_count = int(input())
outfit_price  = float(input())

decor = budget * 0.10

if statists_count > 150:
    outfit_price *= 0.90

total_outfit_price = statists_count * outfit_price
total_price = total_outfit_price + decor
difference = abs(budget - total_price)

if budget >= total_price:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
