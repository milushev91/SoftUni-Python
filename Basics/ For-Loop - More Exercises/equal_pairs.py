n = int(input())

first_pair = 0
equal_pairs = True
counter = 0
max_difference = 0

for _ in range(n):

    num1 = int(input())
    num2 = int(input())

    current_pair = num1 + num2

    counter += 1

    if counter > 2:
        first_pair = counter = 0

    if not first_pair:

        first_pair = current_pair
    else:

        if current_pair != first_pair:
            equal_pairs = False
 
        difference = abs(first_pair - current_pair)
    
        if difference > max_difference:
            max_difference = difference

    
if equal_pairs:
    print(f"Yes, value={first_pair}")
else:
    print(f"No, maxdiff={difference}")
