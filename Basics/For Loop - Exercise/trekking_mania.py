GROUPS = 5

groups_count = int(input())
groups = [0] * GROUPS

for _ in range(groups_count):
    group_count = int(input())
    
    if group_count <= 5:
        groups[0] += group_count
    elif group_count <= 12:
        groups[1] += group_count
    elif group_count <= 25:
        groups[2] += group_count
    elif group_count <= 40:
        groups[3] += group_count
    else:
        groups[4] += group_count

total_count = sum(groups)

for i in range(GROUPS):
    percent = groups[i] / total_count * 100
    print(f"{percent:.2f}%")
