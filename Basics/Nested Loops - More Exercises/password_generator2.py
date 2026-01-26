n = int(input())
l = int(input())

for num1 in range(1, n + 1):
    for num2 in range(1, n + 1):
        for char1 in range(97, 97 + l):
            for char2 in range(97, 97 + l):
                for num3 in range(1, n + 1):
                    if num3 <= num2 or num3 <= num1:
                        continue
                    
                    print(f"{num1}{num2}{chr(char1)}{chr(char2)}{num3}", end=" ")
