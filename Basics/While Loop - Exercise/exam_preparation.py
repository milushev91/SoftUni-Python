poor_grades_limit = int(input())


command = input()
poor_grades_counter = 0
task_counter = 0
sum_grades = 0
last_task = ""

while command != "Enough":
    task_name = command
    grade = float(input())
    task_counter += 1
    last_task = task_name
    sum_grades += grade
    
    if grade <= 4:
        poor_grades_counter += 1
        
        if poor_grades_counter == poor_grades_limit:
            print(f"You need a break, {poor_grades_counter} poor grades.")
            break
    
    command = input()
else:
    avg_grade = sum_grades / task_counter
    print(f"Average score: {avg_grade:.2f}")
    print(f"Number of problems: {task_counter}")
    print(f"Last problem: {last_task}")
    
    
