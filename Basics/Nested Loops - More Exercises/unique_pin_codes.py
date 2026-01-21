START = 1

num1_end = int(input())
num2_end = int(input())
num3_end = int(input())

for num1 in range(START, num1_end + 1):
    if num1 % 2 != 0:
        continue
    
    for num2 in range(2, num2_end + 1):
        if num2 != 2 and num2 != 3 and num2 != 5 and num2 != 7:
            continue
        
        for num3 in range(START, num3_end + 1):
            if num3 % 2 != 0:
                continue   
            
            print(f"{num1} {num2} {num3}")
          
