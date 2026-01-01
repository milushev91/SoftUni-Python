distance = int(input())
time = input()

tax = 0
price_per_km = 0

if distance >= 100:
    price_per_km = 0.06
elif distance >= 20:
    price_per_km = 0.09
else:
    tax = 0.70
    
    if time == "day":
        price_per_km = 0.79
    else:
        price_per_km = 0.90

final_price = distance * price_per_km + tax

print(f"{final_price:.2f}")
