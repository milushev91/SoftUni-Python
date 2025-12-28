world_record_in_seconds = float(input())
distance_in_meters = float(input())
time_per_meter_in_seconds = float(input())

#1. calculate time without delay
time_without_delay_in_seconds = distance_in_meters * time_per_meter_in_seconds

#2. calculate delay time rounded down to nearest integer
delay_time_in_seconds = int((distance_in_meters / 15)) * 12.5

#3. add delay time to time without delay
total_time_in_seconds = time_without_delay_in_seconds + delay_time_in_seconds

#4. compare time to world record and print result

if total_time_in_seconds < world_record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time_in_seconds:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time_in_seconds - world_record_in_seconds:.2f} seconds slower.")
