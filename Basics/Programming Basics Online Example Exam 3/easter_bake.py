# cook your dish here
from math import ceil

SUGGAR_PACKAGE_WEIGHT = 950
FLOUR_PACKAGE_WEIGHT = 750

easter_cakes_count = int(input())

used_sugar = used_flour = 0 
max_sugar_used = max_flour_used = 0

for _ in range(easter_cakes_count):
    easter_cake_sugar = int(input())
    easter_cake_flour = int(input())
    
    used_sugar += easter_cake_sugar
    used_flour += easter_cake_flour
    
    if easter_cake_sugar > max_sugar_used:
        max_sugar_used = easter_cake_sugar
    
    if easter_cake_flour > max_flour_used:
        max_flour_used = easter_cake_flour

sugar_packages_count = ceil(used_sugar / SUGGAR_PACKAGE_WEIGHT)
flour_packages_count = ceil(used_flour / FLOUR_PACKAGE_WEIGHT)

print(f"Sugar: {sugar_packages_count}")
print(f"Flour: {flour_packages_count}")
print(f"Max used flour is {max_flour_used} grams, max used sugar is {max_sugar_used} grams.")



    
    
