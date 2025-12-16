CHICKEN_MENU_PRICE = 10.35 
FISH_MENU_PRICE = 12.40
VEGETARIAN_MENU_PRICE = 8.15
DELIVERY = 2.50

chicken_menus_count = int(input())
fish_menus_count = int(input())
vegetarian_menus_count = int(input())

#calculate menus price 
chicken_menus_price = chicken_menus_count * CHICKEN_MENU_PRICE
fish_menus_price = fish_menus_count * FISH_MENU_PRICE
vegetarian_menus_price = vegetarian_menus_count * VEGETARIAN_MENU_PRICE

menus_price = chicken_menus_price + fish_menus_price + vegetarian_menus_price

#calculate desert price 
desert_price = menus_price * 0.20

#calculate final price menus + desert + delivery
final_price = menus_price + desert_price + DELIVERY

print(final_price)
