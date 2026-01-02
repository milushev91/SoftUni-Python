fuel_type = input()
tank_lv = float(input())

if fuel_type not in ["Diesel", "Gas", "Gasoline"]:
    print("Invalid fuel!")
else:
    fuel_type = fuel_type.casefold()

    if tank_lv >= 25:
        print(f"You have enough {fuel_type}.")
    else:
        print(f"Fill your tank with {fuel_type}!")
