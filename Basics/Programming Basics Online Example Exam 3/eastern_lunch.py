KOZUNAK_PRICE = 3.20  
EGGS_12_CURST_PRICE = 4.35 
COOKIES_KG_PRICE = 5.40 
EGG_PAINT_PRICE = 0.15

kozunaks_count = int(input())
eggs_curst_count = int(input())
cookies_kgs_count = int(input())

kozunaks_price = kozunaks_count * KOZUNAK_PRICE
eggs_price = (eggs_curst_count * EGGS_12_CURST_PRICE) + \
    eggs_curst_count * 12 * EGG_PAINT_PRICE
cookies_price = cookies_kgs_count * COOKIES_KG_PRICE

total_price =  kozunaks_price + eggs_price + cookies_price

print(f"{total_price:.2f}")
