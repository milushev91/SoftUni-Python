# cook your dish here

num = float(input())
abs_num = abs(num)

if num == 0:
    print("zero")
elif num > 0:
    if num < 1:
        print("small positive")
    elif num > 1_000_000:
        print("large positive")
    else:
        print("positive")
else:
    if abs_num < 1:
        print("small negative")
    elif abs_num > 1_000_000:
        print("large negative")
    else:
        print("negative")   
