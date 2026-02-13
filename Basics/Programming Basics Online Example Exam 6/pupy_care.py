available_food = int(input()) * 1000

eaten_food = 0
command = input()

while command != "Adopted":
    daily_food_eaten = int(command)
    eaten_food += daily_food_eaten
    command = input()

difference = abs(available_food - eaten_food)

if available_food >= eaten_food:
    print(f"Food is enough! Leftovers: {difference} grams." )
else:
    print(f"Food is not enough. You need {difference} grams more." )
