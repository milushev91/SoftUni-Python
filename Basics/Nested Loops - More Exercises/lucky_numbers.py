n = int(input())

for num1 in range(1, 10):
    for num2 in range(1, 10):
        for num3 in range(1, 10):
            for num4 in range(1, 10):
                first_digit_sum = num1 + num2
                
                if first_digit_sum != num3 + num4:
                    continue
                
                if n % first_digit_sum != 0:
                    continue
                
                print(f"{num1}{num2}{num3}{num4}", end=" ")
