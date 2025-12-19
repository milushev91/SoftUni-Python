sum_time = sum([int(input()), int(input()), int(input())])

minutes = sum_time // 60 
seconds = sum_time % 60 

print(minutes, end=":")
print(0 if seconds < 10 else "", end="")
print(seconds)
