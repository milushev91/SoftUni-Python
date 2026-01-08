age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

even_year_money = 0
total_money = 0

for year in range(1, age + 1):
    
    if year % 2 != 0:
        total_money += toy_price
    else:
        even_year_money += 10
        total_money += even_year_money
        total_money -= 1 

difference = abs(total_money - washing_machine_price)

print("Yes" if total_money >= washing_machine_price else "No", end=f"! {difference:.2f}")
