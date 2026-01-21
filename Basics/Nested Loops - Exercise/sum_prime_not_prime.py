sum_prime = sum_non_prime = 0
end_loop = False

while not end_loop:
    command = input()
    
    if command == "stop":
        break 
    
    num = int(command)
    
    if num < 0:
        print("Number is negative.")
        continue
    
    if num <= 1:
        sum_non_prime += num 
    else:
        
        for i in range(2, num):
            if num % i == 0:
                sum_non_prime += num 
                break 
        else:
            sum_prime += num
            
print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")
