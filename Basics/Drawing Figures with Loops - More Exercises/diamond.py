from math import ceil

n = int(input())

stars = mid_dashes = 2 if n % 2 == 0 else 1
dashes = (n - stars) // 2
mid = ceil(n / 2)
end = n if n % 2 == 0 else n + 1

for i in range(1, end):
    if i == 1 or i == n:
        stars = 2 if n % 2 == 0 else 1
        print(dashes * "-" + stars * "*" + dashes * "-")
    else:
        stars = 2
        side_dashes = (n - stars - mid_dashes) // 2
        print(side_dashes * "-" + "*" + mid_dashes * "-" + "*" + side_dashes * "-")
        
        if i >= mid:
            mid_dashes -= 2
        else:
            mid_dashes += 2
          
