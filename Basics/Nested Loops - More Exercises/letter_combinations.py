start = ord(input())
end = ord(input())
control = ord(input())
counter = 0

for acii1 in range(start, end + 1):
    if acii1 == control:
        continue
    for acii2 in range(start, end + 1):
        if acii2 == control:
            continue
        for ascii3 in range(start, end + 1):
            if ascii3 == control:
                continue
            counter += 1
            print(f"{chr(acii1)}{chr(acii2)}{chr(ascii3)}", end=" ")
          
print(counter)
