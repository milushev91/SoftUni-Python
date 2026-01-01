from math import ceil, floor

days = int(input())
food_kgs = int(input())
dog_food_kgs_per_day = float(input())
cat_food_kgs_per_day = float(input())
turtle_food_kgs_per_day = float(input()) / 1000

needed_food = days * (dog_food_kgs_per_day + cat_food_kgs_per_day + turtle_food_kgs_per_day)

if food_kgs >= needed_food:
    left_food = food_kgs - needed_food
    print(f"{floor(left_food)} kilos of food left.")
else:

    print(f"{ceil(needed_food - food_kgs)} more kilos of food are needed.")
