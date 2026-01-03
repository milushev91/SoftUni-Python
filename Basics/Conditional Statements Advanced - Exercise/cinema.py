PREMIERE_PRICE = 12
NORMAL_PRICE = 7.50
DISCOUNT_PRICE = 5

type = input()
rows = int(input())
cols = int(input())

price = 0

if type == "Premiere":
    price = PREMIERE_PRICE
elif type == "Normal":
    price = NORMAL_PRICE
else:
    price = DISCOUNT_PRICE

total_seats = rows * cols
income = total_seats * price

print("{:.2f} leva".format(income))
