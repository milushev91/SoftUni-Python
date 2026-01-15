name = input()
year = 1
total_grades = 0
fail_counter = 0

while year <= 12:
    grade = float(input())

    if grade < 4:
        fail_counter += 1
        if fail_counter == 2:
            print(f"{name} has been excluded at {year} grade")
            break
    else:
        total_grades += grade
        year += 1
else:
    avg_grade = total_grades / 12
    print(f"{name} graduated. Average grade: {avg_grade:.2f}")
