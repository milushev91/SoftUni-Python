kill_list = input().split()
kill_position = int(input()) - 1

killed_list = []
kill_index = 0

while kill_list:
    kill_index += kill_position

    while kill_index >= len(kill_list):
        kill_index -= len(kill_list)

    killed_list.append(kill_list.pop(kill_index))

print(f"[{','.join(killed_list)}]")
