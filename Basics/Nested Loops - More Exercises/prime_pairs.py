def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
            
    return True


start1 = int(input())
start2 = int(input())
diffenence1 = int(input())
diffenence2 = int(input())

end1 = start1 + diffenence1 + 1 
end2 = start2 + diffenence2 + 1 

for num1 in range(start1, end1):
    for num2 in range(start2, end2):
        if is_prime(num1) and is_prime(num2):
            print(f"{num1}{num2}")
