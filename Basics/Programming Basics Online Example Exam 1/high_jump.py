goal = int(input().strip())

current_height = goal - 30
jumps_count = 0
fail_counter = 0

while True:
    jump = int(input().strip())
    jumps_count += 1

    if jump > current_height:
        # Успешен скок над летвата
        fail_counter = 0
        last_cleared = current_height

        if current_height == goal:
            # Успешно прескочи желаната височина
            print(f"Tihomir succeeded, he jumped over {last_cleared}cm after {jumps_count} jumps.")
            break

        # Вдигаме летвата за следващия опит
        current_height += 5
    else:
        # Неуспешен скок
        fail_counter += 1
        if fail_counter == 3:
            print(f"Tihomir failed at {current_height}cm after {jumps_count} jumps.")
            break
