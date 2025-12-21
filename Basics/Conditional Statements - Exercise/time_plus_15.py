hours = int(input())
minutes = int(input()) + 15 

if minutes >= 60:
    minutes -= 60
    hours += 1

    if hours > 23:
        hours = 0

print("{}:".format(hours), end="")

if minutes < 10:
    print(0, end="")

print("{}".format(minutes))
