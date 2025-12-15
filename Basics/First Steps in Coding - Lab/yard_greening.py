PRICE_PER_SQ_M = 7.61
DISCOUNT_PERCENT = 0.18

sq_m = float(input())

greening_price = PRICE_PER_SQ_M * sq_m
discount = greening_price * DISCOUNT_PERCENT
final_price = greening_price - discount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")
