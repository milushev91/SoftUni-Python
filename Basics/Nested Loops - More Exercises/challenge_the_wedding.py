men_count = int(input())
women_count = int(input())
tables_count = int(input())

tables_counter = 0
end_loops = False

for male_number in range(1, men_count + 1):
 
    for female_number in range(1, women_count + 1):
        if tables_counter >= tables_count:
            end_loops = True
            break
        
        print(f"({male_number} <-> {female_number})", end=" ")
        
        tables_counter += 1
        
    if end_loops:
        break
