GASOLINE_PRICE = 2.22
DIESEL_PRICE = 2.33
GAS_PRICE = 0.93

fuel_type = input()
amount = float(input())
discount_card = input()

discount = 0
fuel_per_litter_price = 0

if fuel_type == "Gasoline":
    fuel_per_litter_price = GASOLINE_PRICE
    discount = 0.18
elif fuel_type == "Diesel":
    fuel_per_litter_price = DIESEL_PRICE
    discount = 0.12
else:
    fuel_per_litter_price = 0.93
    discount = 0.08

if discount_card == "Yes":
    fuel_per_litter_price -= discount

final_price = amount * fuel_per_litter_price

if 20 <= amount <= 25:
    final_price *= 0.92
elif amount > 25:
    final_price *= 0.90

print(f"{final_price:.2f} lv.")
