last_sector = input()
first_sector_rows = int(input())
odd_row_seats_count = int(input())

sector_start = ord("A")
sector_end = ord(last_sector) + 1
sector_rows = first_sector_rows
seats_counter = 0

for sector_number in range(sector_start, sector_end):
    
    for row in range(1, sector_rows + 1):
        row_seats_count = odd_row_seats_count
        
        if row % 2 == 0:
            row_seats_count = odd_row_seats_count + 2 
        
        for seat in range(97, 97 + row_seats_count):
            print(f"{chr(sector_number)}{row}{chr(seat)}")
            seats_counter += 1
            
    sector_rows += 1

print(seats_counter)
        
        
        
