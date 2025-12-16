NYLON_SQ_M_PRICE = 1.5 
PAINT_LITTER_PRICE = 14.50 
DETERGENT_LITTER_PRICE = 5.00
BAG_PRICE = 0.40

nylon_sq_m = int(input())
paint_litters = int(input())
detergent_litters = int(input())
work_hours = int(input())

nylon_sq_m += 2
paint_litters *= 1.10

nylon_price = nylon_sq_m * NYLON_SQ_M_PRICE
paint_price = paint_litters * PAINT_LITTER_PRICE
detergent_price = detergent_litters * DETERGENT_LITTER_PRICE

materials_price = nylon_price + paint_price + detergent_price + BAG_PRICE
work_per_hour_price = materials_price * 0.30 
work_price = work_per_hour_price * work_hours

total_price = materials_price + work_price

print(total_price)
