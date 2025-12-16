length = float(input()) * 100
width = float(input()) * 100 - 100

length_work_spaces = length // 120
width_work_spaces = width // 70
total_spaces = int(length_work_spaces * width_work_spaces) - 3

print(total_spaces)
