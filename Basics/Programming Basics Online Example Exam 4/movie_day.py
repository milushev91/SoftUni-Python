# cook your dish here
shooting_time = int(input())
sceenes_count = int(input())
sceene_length = int(input())

preparation_time = shooting_time * 0.15
sceenes_time = sceenes_count * sceene_length
total_time = preparation_time + sceenes_time
difference = round(abs(total_time - shooting_time))


if total_time <= shooting_time:
    print(f"You managed to finish the movie on time! You have {difference} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {difference} minutes.")
