days = int(input())
hours = int(input())

total_tax = 0

for day_number in range(1, days + 1):
    daily_price = 0
    
    for hour_number in range(1, hours + 1):
        
        hourly_price = 0
        
        if day_number % 2 == 0 and hour_number % 2 != 0:
            hourly_price = 2.5
        elif day_number % 2 != 0 and hour_number % 2 == 0:
            hourly_price = 1.25
        else:
            hourly_price = 1 
        
        daily_price += hourly_price
        
    print(f"Day: {day_number} - {daily_price:.2f} leva")
    
    total_tax += daily_price

print(f"Total: {total_tax:.2f} leva")
