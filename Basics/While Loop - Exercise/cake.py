cake_width = int(input())
cake_height = int(input())

cake_pcs_count = cake_width * cake_height

command = input()

while command != "STOP":
    current_pcs_count = int(command)
    
    if current_pcs_count > cake_pcs_count:
        print(f"No more cake left! You need {current_pcs_count - cake_pcs_count} pieces more.")
        break
    
    cake_pcs_count -= current_pcs_count
    command = input()

else:
    print(f"{cake_pcs_count} pieces are left." )
