DOG_PACKAGE_PRICE = 2.5
CAT_PACKAGE_PRICE = 4

dog_packages_count = int(input())
cat_packages_count = int(input())

dog_food_price = DOG_PACKAGE_PRICE * dog_packages_count
cat_food_price = CAT_PACKAGE_PRICE * cat_packages_count

total_price = dog_food_price + cat_food_price

print(f"{total_price} lv.")
