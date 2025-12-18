from math import ceil

people_count = int(input())
single_entry_tax = float(input())
sunbed_price = float(input())
umbrella_price = float(input())

total_entry_tax = single_entry_tax * people_count

sunbed_count = ceil(people_count * 0.75)
umbrellas_count = ceil(people_count / 2)

sunbeds_price = sunbed_count * sunbed_price
umbrellas_price = umbrellas_count * umbrella_price

final_price = total_entry_tax + sunbeds_price + umbrellas_price

print(f"{final_price:.2f} lv." )
