n = int(input())
word = input()

strings = [input() for _ in range(n)]
filtered_strings = [string for string in strings if word in string]

print(strings)
print(filtered_strings)
