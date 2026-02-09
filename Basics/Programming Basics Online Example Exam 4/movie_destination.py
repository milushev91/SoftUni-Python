# cook your dish here
PRICES = {
    "Dubai": {
        "Winter": 45_000,
        "Summer": 40_000,
    },
    "Sofia": {
        "Winter": 17_000,
        "Summer": 12_500,
    }, 
    "London": {
        "Winter": 24_000,
        "Summer": 20_250,
    }, 
}

budget = float(input())
destination = input()
season = input()
days_count = int(input())

daily_price = PRICES[destination][season]

if destination == "Dubai":
    daily_price *= 0.70 
elif destination == "Sofia":
    daily_price *= 1.25 

final_price = daily_price * days_count
difference = abs(budget - final_price)

if budget >= final_price:
    print(f"The budget for the movie is enough! We have {difference:.2f} leva left!")
else:
    print(f"The director needs {difference:.2f} leva more!")
