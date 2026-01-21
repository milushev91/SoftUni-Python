main_loop_command = input()

sold_tickets = {
    "student": 0,
    "standard": 0,
    "kid": 0,
}

while main_loop_command != "Finish":
    movie = main_loop_command
    
    tickets_count = int(input())
    taken_spaces = 0
    
    for _ in range(tickets_count):
        command = input()
        
        if command == "End":
            break
        
        taken_spaces += 1
        ticket_type = command
        sold_tickets[ticket_type] += 1
        
    print(f"{movie} - {taken_spaces / tickets_count * 100:.2f}% full.")
    main_loop_command = input()

total_sold_tickets = sum(sold_tickets.values())   

print(f"Total tickets: {total_sold_tickets}")
print(f"{sold_tickets['student'] / total_sold_tickets * 100:.2f}% student tickets.")
print(f"{sold_tickets['standard'] / total_sold_tickets * 100:.2f}% standard tickets.")
print(f"{sold_tickets['kid'] / total_sold_tickets * 100:.2f}% kids tickets.")
    
