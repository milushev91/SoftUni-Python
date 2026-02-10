a1 = int(input())
a2 = int(input())
n = int(input())

for char_num in range(a1, a2):
    if char_num % 2 == 0:
        continue
    
    for num1 in range(1, n):
        for num2 in range(1, int(n / 2)):
            char_sum = num1 + num2 + char_num
            
            if char_sum % 2 == 0:
                continue
            
            print(f"{chr(char_num)}-{num1}{num2}{char_num}")
