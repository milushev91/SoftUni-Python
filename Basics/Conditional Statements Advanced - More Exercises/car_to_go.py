budget = float(input())
season = input()

price = 0
car_class = car_type = ""

if budget <= 100:
    prices = {
        "Summer": ["Cabrio", budget * 0.35],
        "Winter": ["Jeep", budget * 0.65],
    }
    
    car_class = "Economy class"
    car_type, price = prices[season]
    
elif budget <= 500:
    prices = {
        "Summer": ["Cabrio", budget * 0.45],
        "Winter": ["Jeep", budget * 0.80],
    }
    
    car_class = "Compact class"
    car_type, price = prices[season]
    
else:
    car_class = "Luxury class"
    car_type = "Jeep"
    price = budget * 0.90
    
print(f"{car_class}")
print(f"{car_type} - {price:.2f}")
