ROSES_PRICE = 5
DAHLIAS_PRICE = 3.80
TULIPS_PRICE = 2.80
NARCISSUS_PRICE = 3
GLADIOLUS_PRICE = 2.50

flowers_type = input()
flowers_count = int(input())
budget = int(input())

final_price = flowers_count

if flowers_type == "Roses":
    final_price *= ROSES_PRICE

    if flowers_count > 80:
        final_price *= 0.90

elif flowers_type == "Dahlias":
    final_price *= DAHLIAS_PRICE

    if flowers_count > 90:
        final_price *= 0.85

elif flowers_type == "Tulips":
    final_price *= TULIPS_PRICE

    if flowers_count > 80:
        final_price *= 0.85

elif flowers_type == "Narcissus":
    final_price *= NARCISSUS_PRICE

    if flowers_count < 120:
        final_price *= 1.15

elif flowers_type == "Gladiolus":
    final_price *= GLADIOLUS_PRICE

    if flowers_count < 80:
        final_price *= 1.20

difference = f"{abs(budget - final_price):.2f}"

if budget >= final_price:
    print(f"Hey, you have a great garden with {flowers_count} {flowers_type} and {difference} leva left.")
else:
    print(f"Not enough money, you need {difference} leva more.")
