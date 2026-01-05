nights = int(input()) - 1 
room = input()
grade = input()

night_price = 0

if room == "room for one person":
    night_price = 18
elif room == "apartment":
    night_price = 25
    
    if nights < 10:
        night_price *= 0.70
    elif nights <= 15:
        night_price *= 0.65
    else:
        night_price *= 0.50
 
else:
    night_price = 35

    if nights < 10:
        night_price *= 0.90
    elif nights <= 15:
        night_price *= 0.85
    else:
        night_price *= 0.80

if grade == "positive":
    night_price *= 1.25
else:
    night_price *= 0.90

print(f"{night_price * nights:.2f}")
