indexes = input().split()
message_chars = list(input())

output = ""

for idx in indexes:
    char_idx = sum(int(digit) for digit in idx)
    message_chars_length = len(message_chars)
    
    while char_idx >= message_chars_length:
        char_idx -= message_chars_length
    
    output += message_chars.pop(char_idx)
    
print(output)
