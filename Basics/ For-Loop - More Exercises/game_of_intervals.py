moves = int(input())

result = 0 

invalid = group1 = group2 = group3 = group4 = group5 = 0

for _ in range(moves):
    num = int(input())
    
    if 0 <= num <= 9:
        result += num * 0.20
        group1 += 1 
    elif 10 <= num <= 19:
        result += num * 0.30 
        group2 += 1 
    elif 20 <= num <= 29:
        result += num * 0.40
        group3 += 1 
    elif 30 <= num <= 39:
        result += 50
        group4 += 1
    elif 40 <= num <= 50:
        result += 100
        group5 += 1
    else:
        invalid += 1 
        result /= 2

print(f"{result:.2f}")
print(f"From 0 to 9: {group1 / moves * 100:.2f}%")
print(f"From 10 to 19: {group2 / moves * 100:.2f}%")
print(f"From 20 to 29: {group3 / moves * 100:.2f}%")
print(f"From 30 to 39: {group4 / moves * 100:.2f}%")
print(f"From 40 to 50: {group5 / moves * 100:.2f}%")
print(f"Invalid numbers: {invalid / moves * 100:.2f}%")
