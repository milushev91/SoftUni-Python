STEPS_GOAL = 10_000
total_steps = 0 
end_loop = False

while total_steps < STEPS_GOAL:
    command = input()

    if command == "Going home":
        steps = int(input())
        end_loop = True
    else:
        steps = int(command)
    
    total_steps += steps
    
    if end_loop:
        break

difference = abs(total_steps - STEPS_GOAL)

if total_steps >= STEPS_GOAL:
    print("Goal reached! Good job!" )
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")
