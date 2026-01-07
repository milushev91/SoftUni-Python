def calculate_sum(n):
    sum_nums = 0
    
    for _ in range(n):
        num = int(input())
        sum_nums += num 
        
    return sum_nums

num_count = int(input())

right_sum = calculate_sum(num_count)
left_sum = calculate_sum(num_count)

difference = abs(right_sum - left_sum)

if not difference:
    print(f"Yes, sum = {right_sum}")
else:
    print(f"No, diff = {difference}")
