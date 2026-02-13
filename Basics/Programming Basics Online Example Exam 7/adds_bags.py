luggage_price_over_20kg = float(input())
luggage_kgs = float(input())
days_until_travel = int(input())
luggage_count = int(input())

luggage_price = luggage_price_over_20kg

if luggage_kgs < 10:
    luggage_price = luggage_price_over_20kg * 0.20
elif luggage_kgs <= 20:
    luggage_price = luggage_price_over_20kg * 0.50

total_price = luggage_price * luggage_count

if days_until_travel < 7:
    total_price *= 1.40
elif days_until_travel <= 30:
    total_price *= 1.15
else:
    total_price *= 1.10

print(f"The total price of bags is: {total_price:.2f} lv. ")

    
