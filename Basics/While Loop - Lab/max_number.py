command = input()

max_num = float("-inf")

while command != "Stop":
    num = int(command)
    
    if max_num < num:
        max_num = num 
    
    command = input()

print(max_num)
