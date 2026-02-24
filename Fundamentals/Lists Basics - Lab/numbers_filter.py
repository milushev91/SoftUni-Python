# cook your dish hereprint
n = int(input())

number_arrays = {
    "even": [],
    "odd": [],
    "positive": [],
    "negative": [],
}

for _ in range(n):
    num = int(input())
    
    if num % 2 == 0:
        number_arrays["even"].append(num)
    else:
        number_arrays["odd"].append(num)
        
    if num >= 0:
        number_arrays["positive"].append(num)
    else:
        number_arrays["negative"].append(num)

command = input()

print(number_arrays[command])
