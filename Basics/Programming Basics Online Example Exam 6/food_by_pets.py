days = int(input())
available_food = float(input())

total_eaten_food = 0
total_eaten_food_by_dog = total_eaten_food_by_cat = 0
biscuits = 0

for day_number in range(1, days + 1):
    eaten_food_by_dog = int(input())
    eaten_food_by_cat = int(input())
    
    daily_eaten_food = eaten_food_by_dog + eaten_food_by_cat
    
    total_eaten_food_by_dog += eaten_food_by_dog
    total_eaten_food_by_cat += eaten_food_by_cat
    total_eaten_food += daily_eaten_food
    
    if day_number % 3 == 0:
        daily_biscuits = daily_eaten_food * 0.10
        biscuits += daily_biscuits
        
print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{total_eaten_food / available_food * 100:.2f}% of the food has been eaten.")
print(f"{total_eaten_food_by_dog / total_eaten_food * 100:.2f}% eaten from the dog.")
print(f"{total_eaten_food_by_cat / total_eaten_food * 100:.2f}% eaten from the cat.")
    
    
    
