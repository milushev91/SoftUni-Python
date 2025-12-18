REDUCE_TIME_DISTANCE = 120 
REDUCE_TIME_SECONDS = 2.50 

time_to_beat = int(input()) * 60 + int(input())
distance = float(input())
seconds_per_100_m = int(input())

time = (distance / 100) * seconds_per_100_m
time -= (distance / REDUCE_TIME_DISTANCE) * REDUCE_TIME_SECONDS

if time_to_beat >= time:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {time:.3f}.")
else:
    print(f"No, Marin failed! He was {time - time_to_beat:.3f} second slower.")
