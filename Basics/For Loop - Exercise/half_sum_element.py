n = int(input())

max_num = float("-inf")
num_sum = 0

for _ in range(n):
    num = int(input())
    num_sum += num
    
    if num > max_num:
        max_num = num 

num_sum -= max_num  
difference = abs(max_num - num_sum)

if not difference:
    print("Yes")
    print(f"Sum = {num_sum}")
else:
    print("No")
    print("Diff = {}".format(difference))
