BUS_PRICE_PER_TONE = 200
TRUCK_PRICE_PER_TONE = 175
TRAIN_PRICE_PER_TONE = 120

goods_count = int(input())
total_price = total_weight = 0
tones_by_bus = tones_by_truck = tones_by_train = 0

for _ in range(goods_count):
    good_weight = int(input())
    
    #calculate total tones
    total_weight += good_weight
    
    current_price = 0 
    
    if good_weight <= 3:
        current_price = BUS_PRICE_PER_TONE
        tones_by_bus += good_weight
    elif good_weight <= 11:
        current_price = TRUCK_PRICE_PER_TONE
        tones_by_truck += good_weight
    else:
        current_price = TRAIN_PRICE_PER_TONE
        tones_by_train += good_weight
    
    #calculate total price
    total_price += current_price * good_weight

#calculate avg price per tone price / tones
avg_price_per_tone = total_price / total_weight
print(f"{avg_price_per_tone:.2f}")

for item in [tones_by_bus, tones_by_truck, tones_by_train]:
    print(f"{item / total_weight * 100:.2f}%")
