MUSSELS_KG_PRICE = 7.50

mackerel_kg_price = float(input())
sprat_kg_price = float(input())

bonito_kgs = float(input())
horse_mackerel_kgs = float(input())
mussels_kgs = int(input())

bonito_kg_price = mackerel_kg_price + mackerel_kg_price  * 0.60
horse_mackerel_kg_price = sprat_kg_price + sprat_kg_price * 0.80

bonito_price = bonito_kgs * bonito_kg_price
horse_mackerel_price = horse_mackerel_kgs * horse_mackerel_kg_price
mussels_price = mussels_kgs * MUSSELS_KG_PRICE

bill = bonito_price + horse_mackerel_price + mussels_price

print(f"{bill:.2f}")
