from math import ceil

n = int(input())
mid = ceil(n / 2)

for i in range(1, n + 1):
    mid_char = " "
    line = ""
    
    if i == 1 or i == n:
        line = n * 2 * "*"
    else:
        line = "*" + (n * 2 - 2) * "/" + "*"
    
    if i == mid:
        mid_char = "|"
    
    print(line, end="")
    print(mid_char * n, end="")
    print(line)
