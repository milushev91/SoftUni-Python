budget = float(input())
season = input()

price = 0
accomodation_type = location = ""


if budget <= 1000:
    prices = {
        "Summer": ["Alaska", budget * 0.65],
        "Winter": ["Morocco", budget * 0.45],
    }
    
    accomodation_type = "Camp"
    location, price = prices[season]
    
elif budget <= 3000:
    prices = {
        "Summer": ["Alaska", budget * 0.80],
        "Winter": ["Morocco", budget * 0.60],
    }
    
    accomodation_type = "Hut"
    location, price = prices[season]
    
else:
    
    prices = {
        "Summer": ["Alaska"],
        "Winter": ["Morocco"],
    }
    accomodation_type = "Hotel"
    location = prices[season][0]
    price = budget * 0.90
    
print(f"{location} - {accomodation_type} - {price:.2f}")

