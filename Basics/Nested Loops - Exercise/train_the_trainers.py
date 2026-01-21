judges_count = int(input())

sum_grades = 0
presentation_count = 0

command = input()

while command != "Finish":
    name = command
    presentation_count += 1
    presentations_grades = 0
    
    for _ in range(judges_count):
        grade = float(input())
        presentations_grades += grade 
    
    avg_grade = presentations_grades / judges_count
    sum_grades += avg_grade
    
    print(f"{name} - {presentations_grades / judges_count:.2f}.")
    
    command = input()
    
print(f"Student's final assessment is {sum_grades / presentation_count:.2f}." )
    
    
