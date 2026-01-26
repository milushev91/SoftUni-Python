days = int(input())
hours = int(input())

total_tax = 0

for day_number in range(1, days + 1):
    daily_tax = 0
    for hour in range(1, hours + 1):
        if day_number % 2 == 0 and hour % 2 != 0:
            daily_tax += 2.5
        elif day_number % 2 != 0 and hour % 2 == 0:
            daily_tax += 1.25
        else:
            daily_tax += 1 
    
    total_tax += daily_tax
    
    print(f"Day: {day_number} - {daily_tax:.2f} leva")
print(f"Total: {total_tax:.2f} leva")
