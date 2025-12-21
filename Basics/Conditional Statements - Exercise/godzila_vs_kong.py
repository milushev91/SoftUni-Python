budget = float(input())
statists_count = int(input())
statist_outfit_price = float(input())

decor = budget * 0.10

if statists_count > 150:
        statist_outfit_price *= 0.90

statists_price = statists_count * statist_outfit_price
total_cost = statists_price + decor

if budget >= total_cost:
    print("Action!\n" + f"Wingard starts filming with {budget - total_cost:.2f} leva left.")
else:
    print("Not enough money!\n" + f"Wingard needs {total_cost - budget:.2f} leva more.")
