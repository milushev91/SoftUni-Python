CALORIES_BURNT_PER_MIN = 5

walk_minutes = int(input())
walks_count = int(input())
calories_intake = int(input())

burnt_calories = walks_count * walk_minutes * CALORIES_BURNT_PER_MIN
burnt_calories_limit = calories_intake / 2


if burnt_calories >= burnt_calories_limit:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burnt_calories}." )
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burnt_calories}.")
