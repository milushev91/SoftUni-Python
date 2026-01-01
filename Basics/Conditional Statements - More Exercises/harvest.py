from math import ceil, floor

GRAPES_FOR_WINE_PERCENT = 0.40
GRAPES_PER_LITTER_WINE = 2.5

vineyard_sq_m = int(input())
grape_per_sq_m = float(input())
need_wine_litters = int(input())
workers_count = int(input())

#calculate total grapes harvest
total_grapes_harvest = vineyard_sq_m * grape_per_sq_m

#calculate grapes for wine
grapes_for_wine = total_grapes_harvest * GRAPES_FOR_WINE_PERCENT

#calculate wine litters
wine_litters_produced = grapes_for_wine / 2.5

if wine_litters_produced >= need_wine_litters:
    wine_left = wine_litters_produced - need_wine_litters
    wine_per_worker = wine_left / workers_count
    print(f"Good harvest this year! Total wine: {floor(wine_litters_produced)} liters.")
    print(f"{ceil(wine_left)} liters left -> {ceil(wine_per_worker)} liters per person.")
else:
    
    print(f"It will be a tough winter! More {floor(need_wine_litters - wine_litters_produced)} liters wine needed.")
