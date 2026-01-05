ticket_prices = {
    "VIP": 499.99,
    "Normal": 249.99,
}

budget = float(input())
ticket_price = ticket_prices[input()]
group_count = int(input())

transport_price = budget

if 1 <= group_count <= 4:
    transport_price *= 0.75
elif 5 <= group_count <= 9:
    transport_price *= 0.60
elif 10 <= group_count <= 24:
    transport_price *= 0.50
elif 25 <= group_count <= 49:
    transport_price *= 0.40
elif group_count >= 50:
    transport_price *= 0.25

budget -= transport_price
tickets_cost = group_count * ticket_price
difference = f"{abs(budget - tickets_cost):.2f}"

if budget >= tickets_cost:
    print(f"Yes! You have {difference} leva left.")
else:
    print(f"Not enough money! You need {difference} leva.")
