record = float(input())
distance = float(input())
time_per_m = float(input())

time = distance * time_per_m
delay_time = int(distance / 50) * 30
total_time = time + delay_time

if total_time < record:
    print(f" Yes! The new record is {total_time:.2f} seconds.")
else:
    print(f"No! He was {total_time - record:.2f} seconds slower.")
