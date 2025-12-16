PENS_PACKAGE_PRICE = 5.80
MARKERS_PACKAGE_PRICE = 7.20
DETERGENT_LITTER_PRICE = 1.20

pens_packages_count = int(input())
markers_packages_count = int(input())
detergent_litters = int(input())
discount_percent = int(input()) / 100

pens_price = pens_packages_count * PENS_PACKAGE_PRICE
markers_price = markers_packages_count * MARKERS_PACKAGE_PRICE
detergent_price = detergent_litters * DETERGENT_LITTER_PRICE

total_price = pens_price + markers_price + detergent_price
discount = total_price * discount_percent
final_price = total_price - discount

print(final_price)
