n = int(input())
counter = 0
end_loops = False

for row in range(n):
    for col in range(row + 1):
        counter += 1
        
        if row != col:
            print(counter, end=" ")
        else:
            print(counter)
            
        if n == counter:
            end_loops = True
            break
        
    if end_loops:
        break
