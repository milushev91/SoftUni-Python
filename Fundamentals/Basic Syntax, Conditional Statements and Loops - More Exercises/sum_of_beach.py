# cook your dish here
string = input().casefold()
words = ["sand", "water", "fish", "sun"]
counter = 0

for word in words:
    counter += string.count(word)

print(counter)
