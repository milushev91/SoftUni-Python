text = input().casefold()

vowel_sum = 0

vowel_points = {
    "a": 1,
    "e": 2,
    "i": 3,
    "o": 4,
    "u": 5,
}

for char in text:
   
    if char in vowel_points:
        vowel_sum += vowel_points[char]

print(vowel_sum)
