start = int(input())
end = int(input())
magic_number = int(input())

counter = 0 
stop_loops = False

for num1 in range(start, end + 1):
    for num2 in range(start, end + 1):
        counter += 1 
        sum_nums = num1 + num2
        
        if sum_nums == magic_number:
            print(f"Combination N:{counter} ({num1} + {num2} = {magic_number})")
            stop_loops = True
            break
        
    if stop_loops:
        break
else:
    print(f"{counter} combinations - neither equals {magic_number}")
