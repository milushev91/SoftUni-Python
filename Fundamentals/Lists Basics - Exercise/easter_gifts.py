# cook your dish here
gifts = input().split()

command = input()

while command != "No Money":
    line = command.split()
    
    command, gift = line[:2]
    gifts_length = len(gifts)
    
    if command == "OutOfStock":
        
        for idx in range(gifts_length):
            itter_gift = gifts[idx]
            
            if itter_gift == gift:
                gifts[idx] = None
    
    elif command == "Required":
        index = int(line[2])
        
        if 0 <= index < gifts_length:
            gifts[index] = gift
    
    else:
        gifts[-1] = gift
    
    command = input()

[print(gift, end=" ") for gift in gifts if gift]
