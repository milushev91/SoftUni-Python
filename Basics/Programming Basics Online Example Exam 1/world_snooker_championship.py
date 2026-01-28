stage = input()
ticket_type = input()
tickets_count = int(input())
picture = input()

price = 0
has_picture_tax = False

if stage == "Quarter final":
    if ticket_type == "Standard":
        price = 55.50
    elif ticket_type == "Premium":
        price = 105.20
    elif ticket_type == "VIP":
        price = 118.90
elif stage == "Semi final":
    if ticket_type == "Standard":
        price = 75.88
    elif ticket_type == "Premium":
        price = 125.22
    elif ticket_type == "VIP":
        price = 300.40
elif stage == "Final":
    if ticket_type == "Standard":
        price = 110.10
    elif ticket_type == "Premium":
        price = 160.66
    elif ticket_type == "VIP":
        price = 400

total_price = price * tickets_count

picture_tax = tickets_count * 40

if total_price > 4000:
    total_price *= 0.75
    picture_tax = 0
elif total_price > 2500:
    total_price *= 0.90

if picture == "N":
    picture_tax = 0

final_price = total_price + picture_tax
print(f"{final_price:.2f}")
