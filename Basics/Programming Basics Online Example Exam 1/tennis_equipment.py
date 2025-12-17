from math import floor, ceil 

tennis_rocket_price = float(input())

tennis_rockets_count = int(input())
sneakers_count = int(input())

tennis_rockets_price = tennis_rocket_price * tennis_rockets_count

sneakers_price = (tennis_rocket_price / 6) * sneakers_count

other_equipment = (tennis_rockets_price + sneakers_price) * 0.20

total_price = tennis_rockets_price + sneakers_price + other_equipment

player_share = floor(total_price) / 8
sponsors_share = ceil(total_price * 0.875)

print(f"Price to be paid by Djokovic {int(player_share)}")
print(f"Price to be paid by sponsors {sponsors_share}")
