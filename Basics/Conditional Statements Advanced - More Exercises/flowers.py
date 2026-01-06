ARRAGMENT_PRICE = 2

chrysanthemums_count = int(input())
roses_count = int(input())
tuplips_count = int(input())
season = input()
is_a_holiday = input()

flower_prices = [3.75, 4.50, 4.15]

chrysanthemums_price = roses_price = tuplips_price = 0

if season == "Spring" or season == "Summer":
    flower_prices = [2.00, 4.10, 2.50]

bouquet_price = chrysanthemums_count * flower_prices[0] + roses_count * flower_prices[1]\
    + tuplips_count * flower_prices[2]

if is_a_holiday == "Y":
    bouquet_price *= 1.15

if tuplips_count > 7 and season == "Spring":
    bouquet_price *= 0.95

if roses_count >= 10 and season == "Winter":
    bouquet_price *= 0.90

if chrysanthemums_count + roses_count + tuplips_count > 20:
    bouquet_price *= 0.80

bouquet_price += ARRAGMENT_PRICE
    
print("{:.2f}".format(bouquet_price))
