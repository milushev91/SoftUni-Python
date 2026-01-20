n = int(input())

sum_numbers = 0
for _ in range(n):
    num = int(input())
    sum_numbers += num 

avg = sum_numbers / n
print(f"{avg:.2f}")
