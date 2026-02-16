ball_mapper = {
    "red": lambda x: x + 5,
    "orange": lambda x: x + 10,
    "yellow": lambda x: x + 15,
    "white": lambda x: x + 20,
    "black": lambda x: int(x / 2)
}

balls_counter = {
    "red": 0,
    "orange": 0,
    "yellow": 0,
    "white": 0,
    "others": 0,
    "black": 0,
}

balls_count = int(input())
score = 0 

for _ in range(balls_count):
    
    color = input()
    
    if color not in balls_counter:
        balls_counter["others"] += 1 
        continue
    
    score = ball_mapper[color](score)
    balls_counter[color] += 1

print(f"Total points: {score}")

for key, value in balls_counter.items():
    if key == "others":
        break
    
    color = key.title()
    print(f"{color} balls: {value}")

print(f"Other colors picked: {balls_counter['others']}")
print(f"Divides from black balls: {balls_counter['black']}")
    
