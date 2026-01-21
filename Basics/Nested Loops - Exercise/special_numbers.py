n = int(input())
start = 1111
end = 9999

for num in range(start, end + 1):
    str_num = str(num)
    
    for digit in str_num:
        int_digit = int(digit)
        
        
        if int_digit == 0 or n % int_digit != 0:
            break 
    else:
        print(num, end=" ")
