GREEN_PAINT_CONSUMPTION_PER_SQ_M = 3.4
RED_PAINT_CONSUMPTION_PER_SQ_M = 4.3

x = float(input())
y = float(input())
h = float(input())

rectangle_sides = (x * y) * 2
square_sides = (x ** 2) * 2
roof_triangle_sides_sq_m = x * h

green_paint_consumption = ((square_sides - 2.4) + (rectangle_sides - 4.5)) \
    / GREEN_PAINT_CONSUMPTION_PER_SQ_M
red_paint_consumption = (roof_triangle_sides_sq_m + rectangle_sides) / \
    RED_PAINT_CONSUMPTION_PER_SQ_M

print(f"{green_paint_consumption:.2f}")
print(f"{red_paint_consumption:.2f}")
