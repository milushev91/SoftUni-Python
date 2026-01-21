start = int(input())
end = int(input())

for num in range(start, end + 1):
    even_sum = odd_sum = 0
    for index, digit in enumerate(str(num)):
        int_digit = int(digit)
        
        if index % 2 == 0:
            even_sum += int_digit
        else:
            odd_sum += int_digit
    
    if even_sum == odd_sum:
        print(num, end=" ")
