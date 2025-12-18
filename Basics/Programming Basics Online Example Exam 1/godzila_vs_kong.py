budget = float(input())
statists_count = int(input())
outfit_price = float(input())

decor = budget * 0.10 

if statists_count > 150:
    outfit_price *= 0.90
  
statits_cost = statists_count * outfit_price 
total_cost = statits_cost + decor

if total_cost > budget:
    print("Not enough money!")
    print(f"Wingard needs {total_cost - budget:.2f} leva more.")
else:
    print("Action!" )
    print(f"Wingard starts filming with {budget - total_cost:.2f} leva left.")

