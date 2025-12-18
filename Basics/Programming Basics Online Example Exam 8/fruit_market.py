strawberries_kg_price = float(input())

bananas_kgs = float(input())
oranges_kgs = float(input())
raspberries_kgs = float(input())
strawberries_kgs = float(input())

raspberries_kg_price = strawberries_kg_price / 2 
oranges_kg_price = raspberries_kg_price - raspberries_kg_price * 0.40
bananas_kg_price = raspberries_kg_price - raspberries_kg_price * 0.80

strawberries_price = strawberries_kgs * strawberries_kg_price
raspberries_price = raspberries_kgs * raspberries_kg_price
bananas_price = bananas_kgs * bananas_kg_price 
oranges_price = oranges_kgs * oranges_kg_price

total_price = strawberries_price + raspberries_price + bananas_price + oranges_price

print(f"{total_price:.2f}")
