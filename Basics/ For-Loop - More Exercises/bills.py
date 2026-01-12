MONTHLY_WATER_PRICE = 20
MONTHLY_INTERNET_PRICE = 15

months = int(input())

el_total_price = others_total_price = 0
water_total_price = months * MONTHLY_WATER_PRICE
internet_total_price = months * MONTHLY_INTERNET_PRICE

for _ in range(months):
    el_price = float(input())
    
    el_total_price += el_price
    others_total_price += (el_price + MONTHLY_WATER_PRICE + MONTHLY_INTERNET_PRICE) * 1.20

total_price = el_total_price + water_total_price + internet_total_price + others_total_price
monthly_price = total_price / months

print(f"Electricity: {el_total_price:.2f} lv")
print(f"Water: {water_total_price:.2f} lv")
print(f"Internet: {internet_total_price:.2f} lv")
print(f"Other: {others_total_price:.2f} lv")
print(f"Average: {monthly_price:.2f} lv")
