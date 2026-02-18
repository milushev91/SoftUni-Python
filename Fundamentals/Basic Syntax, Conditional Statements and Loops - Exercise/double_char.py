command = input()

while command != "End":
    string = command
    
    if string != "SoftUni":
        for char in string:
            print(char * 2, end="")
        print()
    
    command = input()
