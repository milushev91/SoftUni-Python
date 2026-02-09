DISCOUNT_PERCENTS = {
    "Thrones": 0.5,
    "Lucifer": 0.4,	
    "Protector": 0.3,
    "TotalDrama": 0.2,
    "Area": 0.1,
}

budget = float(input())
series_count = int(input())

series_price = 0

for _ in range(series_count):
    name = input()
    price = float(input())
    
    if name in DISCOUNT_PERCENTS:
        price -= price * DISCOUNT_PERCENTS[name]
    
    series_price += price

difference = f"{abs(budget - series_price):.2f}"

if budget >= series_price:
    print(f"You bought all the series and left with {difference} lv.")
else:
    print(f"You need {difference} lv. more to buy the series!")
    
