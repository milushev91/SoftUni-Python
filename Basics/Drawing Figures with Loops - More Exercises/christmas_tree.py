n = int(input())

print(" " * n + " |")

for i in range(1, n + 1):
    spaces = n - i
    print(" " * spaces + "*" * i + " | " + "*" * i + " " * spaces)
