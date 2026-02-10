budget = float(input())
nights_count = int(input())
night_price = float(input())
other_costs_percent = int(input()) / 100

if nights_count > 7:
    night_price *= 0.95

price = nights_count * night_price + other_costs_percent * budget
difference = f"{abs(budget - price):.2f}"

if budget >= price:
    print(f"Ivanovi will be left with {difference} leva after vacation.")
else:
    print(f"{difference} leva needed.")


            
