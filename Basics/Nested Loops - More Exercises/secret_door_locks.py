end1 = int(input())
end2 = int(input())
end3 = int(input())

for num1 in range(2, end1 + 1, 2):
    for num2 in range(1, end2 + 1):
        if num2 != 2 and num2 != 3 and num2 != 5 and num2 != 7:
            continue 
        for num3 in range(2, end3 + 1, 2):
            print(f"{num1} {num2} {num3}")
