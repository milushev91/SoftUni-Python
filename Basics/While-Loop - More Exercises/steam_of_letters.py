command = input()

output = ""
command_letters = {
    "c": 0,
    "o": 0,
    "n": 0,
}

while command != "End":
    letter = command
    
    if letter.isalpha():
        
        if letter in "con":
            
            if command_letters[letter] == 1:
                command_letters_count = 0
                
                for command_letter in command_letters:
                    command_letters_count += command_letters[command_letter]
                
                if command_letters_count == 3:
                    print(f"{output} ", end="")
                    
                    for command_letter in command_letters:
                        command_letters[command_letter] = 0
                    output = ""
                else:
                    output += letter
                
            else:
                command_letters[letter] = 1
                
                command_letters_count = 0
                for command_letter in command_letters:
                    command_letters_count += command_letters[command_letter]
                    
                if command_letters_count == 3:
                    print(f"{output} ", end="")
                    
                    for command_letter in command_letters:
                        command_letters[command_letter] = 0
                    output = ""
        else:
            output += letter 
    
    command = input()
