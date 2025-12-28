from math import ceil

series_name = input()
episode_length = int(input())
break_length = int(input())

lunch_time = break_length / 8 
rest_time = break_length / 4 

time_for_watching = break_length - (lunch_time + rest_time)

if time_for_watching >= episode_length:
    print(f"You have enough time to watch {series_name} and left with {ceil(time_for_watching - episode_length)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(episode_length - time_for_watching)} more minutes.")
