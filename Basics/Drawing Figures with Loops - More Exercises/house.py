from math import ceil

n = int(input())
mid = ceil(n / 2)
passed_mid = False
stars = 1 if n % 2 != 0 else 2

for i in range(1, n + 1):
    
    if i < mid:
        dashes = int((n - stars )/ 2)
        print(dashes * "-" + stars * "*"  + dashes * "-")
        stars += 2
    
    elif i == mid:
        print("*" * n)
        passed_mid = True

    elif passed_mid:
        print("|" + ((n - 2) * "*") + "|")
    
    
        

        

    
