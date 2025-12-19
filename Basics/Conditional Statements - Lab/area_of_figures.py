from math import pi

figure = input()
area = 0

if figure == "square":
    side_length = float(input())
    area = side_length ** 2

elif figure == "rectangle":
    a = float(input())
    b = float(input())
    
    area = a * b 

elif figure == "circle":
    radius = float(input())
    area = pi * radius ** 2

elif figure == "triangle":
    side_length = float(input())
    height = float(input())
    
    area = side_length * height / 2

print(f"{area:.3f}")
