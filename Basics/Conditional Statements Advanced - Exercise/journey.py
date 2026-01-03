budget = float(input())
season = input()

accommodation_type = destination = ""
accommodation_percent = 0

if budget > 1000:
    accommodation_type = "Hotel"
    destination = "Europe"
    accommodation_percent = 0.90
else:
    if season == "summer":
        accommodation_type = "Camp"

        if budget <= 100:
            destination = "Bulgaria"
            accommodation_percent = 0.30
        else:
            destination = "Balkans"
            accommodation_percent = 0.40
    else:
        accommodation_type = "Hotel"

        if budget <= 100:
            destination = "Bulgaria"
            accommodation_percent = 0.70
        else:
            destination = "Balkans"
            accommodation_percent = 0.80

accommodation_price = budget * accommodation_percent

print(f"Somewhere in {destination}")
print(f"{accommodation_type} - {accommodation_price:.2f}")
