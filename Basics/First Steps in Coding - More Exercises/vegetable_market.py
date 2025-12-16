EURO = 1.94

vegetables_kg_price = float(input())
fruit_kg_price = float(input())

vegetables_kgs = int(input())
fruit_kgs = int(input())

vegerables_price = vegetables_kgs * vegetables_kg_price
fruits_price = fruit_kgs * fruit_kg_price

bgn_price= vegerables_price + fruits_price
euro_price = bgn_price/ EURO

print(f"{euro_price:.2f}")
