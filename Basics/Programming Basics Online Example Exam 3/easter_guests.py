from math import ceil

EASTER_CAKE_PRICE = 4
EGG_PRICE = 0.45

guest_count = int(input())
budget = int(input())

easter_cakes_count = ceil(guest_count / 3)
eggs_count = guest_count * 2

easter_cakes_price = easter_cakes_count * EASTER_CAKE_PRICE
eggs_price = eggs_count * EGG_PRICE

total_price = easter_cakes_price + eggs_price
difference = abs(budget - total_price)


if budget >= total_price:
    print(f"Lyubo bought {easter_cakes_count} Easter bread and {eggs_count} eggs.")
    print(f"He has {difference:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {difference:.2f} lv. more.")
