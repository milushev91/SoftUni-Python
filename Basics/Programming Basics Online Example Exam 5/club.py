# cook your dish here
wanted_income = float(input())

income = 0

command = input()

while command != "Party!":
    coctail_name = command
    coctail_number = int(input())
    
    order_price = len(coctail_name) * coctail_number
    
    if order_price % 2 != 0:
        order_price *= 0.75
    
    income += order_price
    
    if income >= wanted_income:
        print("Target acquired.")
        break
    
    command = input()
else:
    print(f"We need {wanted_income - income:.2f} leva more.")

print(f"Club income - {income:.2f} leva.")


