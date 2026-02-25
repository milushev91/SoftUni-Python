counter = 0
line = input().split(", ")
output = [int(num) for num in line if num != "0"]
output.extend([0] * (len(line) - len(output)))
print(output)
