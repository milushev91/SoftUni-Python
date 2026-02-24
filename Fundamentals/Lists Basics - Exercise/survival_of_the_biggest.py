numbers = [int(num) for num in input().split()]
n = int(input())

for _ in range(n):
    numbers.remove(min(numbers))

print(*numbers, sep=", ")
