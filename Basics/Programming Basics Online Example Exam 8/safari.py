# cook your dish here
PRICE_PER_LITTER = 2.10
GUIDER_PRICE = 100

budget = float(input())
needed_fuel = float(input())
day = input()

fuel_cost = needed_fuel * PRICE_PER_LITTER
total_cost = GUIDER_PRICE + fuel_cost
discount = 0 

if day == "Saturday":
    discount = total_cost * 0.10
else:
    discount = total_cost * 0.20

final_price = total_cost - discount
difference = abs(budget - final_price)

if budget >= final_price:
    print(f"Safari time! Money left: {difference:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {difference:.2f} lv.")
