# cook your dish here
n = int(input())
start = 97
end = 97 + n

for acii_1 in range(start, end):
    for acii_2 in range(start, end):
        for acii_3 in range(start, end):
            print(f"{chr(acii_1)}{chr(acii_2)}{chr(acii_3)}")
