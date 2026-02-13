# cook your dish here
GYM_PRICES = {
    "Gym": {
        "m": 42,
        "f": 35,
    },
    "Boxing": {
        "m": 41,
        "f": 37,
    },
    "Yoga": {
        "m": 45,
        "f": 42,
    },
    "Zumba": {
        "m": 34,
        "f": 31,
    },
    "Dances": {
        "m": 51,
        "f": 53,
    },
    "Pilates": {
        "m": 39,
        "f": 37,
    }
}

available_money = float(input())
gender = input()
age = int(input())
sport = input()

price = GYM_PRICES[sport][gender]

if age <= 19:
    price *= 0.80
    
if available_money >= price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${price - available_money:.2f} more.")
