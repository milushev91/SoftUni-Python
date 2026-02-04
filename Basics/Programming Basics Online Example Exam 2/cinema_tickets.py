# cook your dish here
command = input()

tickets_info = {
    "student": 0,
    "standard": 0,
    "kid": 0,
}

while command != "Finish":
    movie_name = command
    seats = int(input())
    sold_tickets = 0
    
    for _ in range(seats):
        ticket_type = input()
        if ticket_type == "End":
            break
        sold_tickets += 1
        tickets_info[ticket_type] += 1 

    print(f"{movie_name} - {sold_tickets / seats * 100:.2f}% full.")
    
    command = input()

total_tickets = sum(tickets_info.values())
print(f"Total tickets: {total_tickets}")
print(f"{tickets_info['student'] / total_tickets * 100:.2f}% student tickets.")
print(f"{tickets_info['standard'] / total_tickets * 100:.2f}% standard tickets.")
print(f"{tickets_info['kid'] / total_tickets * 100:.2f}% kids tickets.")

        
        
        
    
