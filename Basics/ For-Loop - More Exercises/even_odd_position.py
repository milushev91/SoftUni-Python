n = int(input())
    
odd_sum = even_sum = 0 
odd_min = even_min = float("inf")
odd_max = even_max = float("-inf")
is_there_odd = is_there_even = False
    
for pos in range(1, n + 1):
    num = float(input())
    
    if pos % 2 == 0:
        is_there_even = True
        even_sum += num 
        
        if even_min > num:
            even_min = num 
            
        if even_max < num:
            even_max = num
    else:
        odd_sum += num 
        is_there_odd = True
        
        if odd_min > num:
            odd_min = num 
        
        if odd_max < num:
            odd_max = num

print(f"OddSum={odd_sum:.2f},")
print(f"OddMin={odd_min:.2f}," if is_there_odd else "OddMin=No,")
print(f"OddMax={odd_max:.2f}," if is_there_odd else "OddMax=No,")
print(f"EvenSum={even_sum:.2f},")
print(f"EvenMin={even_min:.2f}," if is_there_even else "EvenMin=No,")
print(f"EvenMax={even_max:.2f}" if is_there_even else "EvenMax=No")
