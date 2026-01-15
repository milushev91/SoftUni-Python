command = input()

min_num = float("inf")

while command != "Stop":
    num = int(command)
    
    if min_num > num:
        min_num = num
    
    command = input()

print(min_num)
