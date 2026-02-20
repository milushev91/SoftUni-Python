n = int(input())

for i in range(1, n + 1):
    
    sum_digits = sum([int(digit) for digit in str(i)])
    is_true = False
    
    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        is_true = True
    
    print(f"{i} -> {is_true}")
