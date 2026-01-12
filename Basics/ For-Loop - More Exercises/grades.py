students_count = int(input())

sum_grades = 0
fail_count = poor_count = good_count = top_count = 0

for _ in range(students_count):
    grade = float(input())
    
    sum_grades += grade
    
    if grade < 3:
        fail_count += 1 
    elif grade < 4:
        poor_count += 1 
    elif grade < 5:
        good_count += 1 
    else:
        top_count += 1

print(f"Top students: {top_count / students_count * 100:.2f}%")
print(f"Between 4.00 and 4.99: {good_count / students_count * 100:.2f}%")
print(f"Between 3.00 and 3.99: {poor_count / students_count * 100:.2f}%")
print(f"Fail: {fail_count / students_count *100:.2f}%")
print(f"Average: {sum_grades / students_count:.2f}")
