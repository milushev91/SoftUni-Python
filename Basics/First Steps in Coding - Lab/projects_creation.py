TIME_PER_PROJECT = 3

name = input()
projects_count = int(input())

time_needed = TIME_PER_PROJECT * projects_count

print(f"The architect {name} will need {time_needed} hours to complete {projects_count} project/s.")
