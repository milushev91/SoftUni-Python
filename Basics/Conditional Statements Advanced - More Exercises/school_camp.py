season = input()
group_type = input()
students_count = int(input())
nights = int(input())

night_price = 0
sport = ""

if group_type == "girls":
    
    if season == "Winter":
        sport = "Gymnastics"
        night_price = 9.60
    elif season == "Spring":
        sport = "Athletics"
        night_price = 7.20
    else:
        sport = "Volleyball"
        night_price = 15

elif group_type == "boys":
    
    if season == "Winter":
        sport = "Judo"
        night_price = 9.60
    elif season == "Spring":
        sport = "Tennis"
        night_price = 7.20
    else:
        sport = "Football"
        night_price = 15    
    
else:
    
    if season == "Winter":
        night_price = 10
        sport = "Ski"
    elif season == "Spring":
        night_price = 9.50
        sport = "Cycling"
    else:
        sport = "Swimming"
        night_price = 20
    
accomodation_price = night_price * nights * students_count

if students_count >= 50:
    accomodation_price *= 0.50
elif students_count >= 20:
    accomodation_price *= 0.85
elif 10 <= students_count <= 20:
    accomodation_price *= 0.95

print(f"{sport} {accomodation_price:.2f} lv.")
