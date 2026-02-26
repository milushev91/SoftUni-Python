def calculate_car_time(car_times, start, end, step):
    total_time = 0
    for idx in range(start, end, step):
        current_time = car_times[idx]
        total_time += current_time
        
        if current_time == 0:
            total_time *= 0.80
        
    return total_time

times = [int(num) for num in input().split()]
times_length = len(times)
midd_idx =  times_length// 2

left_car_time = calculate_car_time(times[:midd_idx], start=0, end=midd_idx, step=1)
right_car_time = calculate_car_time(times[midd_idx + 1:], start=midd_idx - 1, end=-1, step= -1)

if left_car_time <= right_car_time:
    print(f"The winner is left with total time: {left_car_time:.1f}")
else:
    print(f"The winner is right with total time: {right_car_time:.1f}")



