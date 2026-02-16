start1, start2, start3, start4 = [int(digit) for digit in input()]
end1, end2, end3, end4 = [int(digit) for digit in input()]

for num1 in range(start1, end1 + 1):
    if num1 % 2 == 0:
        continue
    for num2 in range(start2, end2 + 1):
        if num2 % 2 == 0:
            continue
        for num3 in range(start3, end3 + 1):
            if num3 % 2 == 0:
                continue
            for num4 in range(start4, end4 + 1):
                if num4 % 2 == 0:
                    continue
                print(f"{num1}{num2}{num3}{num4}", end=" ")
