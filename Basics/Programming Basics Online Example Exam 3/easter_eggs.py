eggs_count = int(input())

colored_eggs_statistics = {
    "red": 0,
    "orange": 0,
    "blue": 0,
    "green": 0,
}

for _ in range(eggs_count):
    color = input()
    
    colored_eggs_statistics[color] += 1 

max_count = 0
max_count_color = None

for key, value in colored_eggs_statistics.items():
    print(f"{key.title()} eggs: {value}")
    
    if value > max_count:
        max_count = value
        max_count_color = key
        
print(f"Max eggs: {max_count} -> {max_count_color}")
