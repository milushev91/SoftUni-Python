budget = float(input())
flour_kg_price = float(input())

eggs_pack_price = flour_kg_price * 0.75
milk_litter_price = (flour_kg_price * 1.25) * 0.25

easter_bread_price = flour_kg_price + eggs_pack_price + milk_litter_price
colored_eggs_count = 0
easter_bread_count = 0

while budget > easter_bread_price:
    budget -= easter_bread_price
    colored_eggs_count += 3 
    easter_bread_count += 1
    
    if easter_bread_count % 3 == 0:
        colored_eggs_count -= easter_bread_count - 2

print(f"You made {easter_bread_count} loaves of Easter bread! Now you have {colored_eggs_count} eggs and {budget:.2f}BGN left.")
