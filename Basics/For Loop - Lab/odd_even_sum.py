n = int(input())

even_positions_sum  = odd_positions_sum = 0

for i in range(n):
    num = int(input())
    
    if i % 2 == 0:
        even_positions_sum += num
    else:
        odd_positions_sum += num 

difference = abs(even_positions_sum - odd_positions_sum)

if not difference:
    print("Yes")
    print("Sum = {}".format(even_positions_sum))
else:
    print("No")
    print("Diff = {}".format(difference))
    
