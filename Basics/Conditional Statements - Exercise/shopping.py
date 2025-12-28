VIDEO_CARD_PRICE = 250

budget = float(input())

video_cards_count = int(input())
cpus_count = int(input())
rams_count = int(input())

video_cards_price = video_cards_count * VIDEO_CARD_PRICE
cpu_price = video_cards_price * 0.35
ram_price = video_cards_price * 0.10

cpus_price = cpus_count * cpu_price
rams_price = rams_count * ram_price

total_price = video_cards_price + cpus_price + rams_price

if video_cards_count > cpus_count:
    total_price *= 0.85

if budget >= total_price:
    print(f"You have {budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")
