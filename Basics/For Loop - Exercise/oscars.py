NOMINE_POINTS = 1250.5

actor_name = input()
start_points = float(input())
judges_count = int(input())

total_points = start_points

for _ in range(judges_count):
    judge_name = input()
    judge_points = float(input())
    
    points = (len(judge_name) * judge_points) / 2
    total_points += points
    
    if total_points > NOMINE_POINTS:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break
else:
    print(f"Sorry, {actor_name} you need {NOMINE_POINTS - total_points:.1f} more!")
