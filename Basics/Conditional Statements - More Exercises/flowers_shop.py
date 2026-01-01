from math import ceil, floor

MAGNOLIAS_PRICE = 3.25
HYACINTHS_PRICE = 4
ROSES_PRICE = 3.50
CACTI_PRICE = 8
TAX_PERCENT = 0.05

magnolias_count = int(input())
hyacinths_count = int(input())
roses_count = int(input())
cacti_count = int(input())
gift_price = float(input())

magnolias_price = magnolias_count * MAGNOLIAS_PRICE
hyacinths_price = hyacinths_count * HYACINTHS_PRICE
roses_price = roses_count * ROSES_PRICE
cacti_price = cacti_count * CACTI_PRICE

income = magnolias_price + hyacinths_price + roses_price + cacti_price
tax = income * TAX_PERCENT

final_income = income - tax

difference = abs(final_income - gift_price)

if final_income >= gift_price:
    print(f"She is left with {floor(difference)} leva.")
else:
    print(f"She will have to borrow {ceil(difference)} leva.")
