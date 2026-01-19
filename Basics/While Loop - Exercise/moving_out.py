space_width = int(input())
space_length= int(input())
space_height = int(input())

free_space = space_width * space_length * space_height

command = input()

while command != "Done":
    boxes_count = int(command)
    
    if boxes_count > free_space:
        print(f"No more free space! You need {boxes_count - free_space} Cubic meters more.")
        break
    
    free_space -= boxes_count
    command = input()
else:
    print(f"{free_space} Cubic meters left.")
