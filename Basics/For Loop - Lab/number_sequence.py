n = int(input())

min_num = float("inf")
max_num = float("-inf")

for _ in range(n):
    num = int(input())
    
    if max_num < num:
        max_num = num 
    
    if min_num > num:
        min_num = num 
    
print(f"Max number: {max_num}")
print(f"Min number: {min_num}")
