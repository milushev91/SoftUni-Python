guest_count = int(input())
cover_price = float(input())
budget = float(input())

total_price = guest_count * cover_price

if 10 <= guest_count <= 15:
    total_price *= 0.85
elif 15 < guest_count <= 20:
    total_price *= 0.80
elif guest_count > 20:
    total_price *= 0.75

total_price += budget * 0.10
difference = abs(total_price - budget)

if budget >= total_price:
    print(f"It is party time! {difference:.2f} leva left.")
else:
    print(f"No party! {difference:.2f} leva needed.")
