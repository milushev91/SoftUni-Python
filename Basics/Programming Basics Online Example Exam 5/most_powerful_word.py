# cook your dish here
vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
strongest_word = ""
strongest_word_points = 0

command = input()

while command != "End of words":
    word = command
    word_length = len(word)
    word_points = 0
    
    for letter in word:
        word_points += ord(letter)
    
    if word[0] in vowels:
        word_points *= word_length
    else:
        word_points /= int(word_length)
    
    if word_points > strongest_word_points:
        strongest_word_points = word_points
        strongest_word = word
        
    command = input()

print(f"The most powerful word is {strongest_word} - {strongest_word_points}" )
