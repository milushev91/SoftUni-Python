month = input()
nights = int(input())

studio_price = apartament_price = 0

if month == "May" or month == "October":
    studio_price = 50
    apartament_price = 65
    
    if nights > 14:
        studio_price *= 0.70
    elif nights > 7:
        studio_price *= 0.95

elif month == "June" or month == "September":
    studio_price = 75.2
    apartament_price = 68.70
    
    if nights > 14:
        studio_price *= 0.80
    
else:
    studio_price = 76
    apartament_price = 77

if nights > 14:
    apartament_price *= 0.90

print(f"Apartment: {nights * apartament_price:.2f} lv.")
print(f"Studio: {nights * studio_price:.2f} lv.")

