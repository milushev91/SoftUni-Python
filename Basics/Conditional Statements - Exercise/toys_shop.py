PUZZLE_PRICE = 2.60
TALKING_DOLL_PRICE = 3
TEDDY_BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2

tour_price = float(input())
puzzles_count = int(input())
talking_dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzles_income = puzzles_count * PUZZLE_PRICE
talking_dolls_icome = talking_dolls_count * TALKING_DOLL_PRICE
teddy_bears_income = teddy_bears_count * TEDDY_BEAR_PRICE
minions_income = minions_count * MINION_PRICE
trucks_income = trucks_count * TRUCK_PRICE

total_income = (puzzles_income + talking_dolls_icome + teddy_bears_income +
                minions_income + trucks_income)

toys_count = puzzles_count + talking_dolls_count + teddy_bears_count + minions_count + trucks_count

if toys_count >= 50:
    total_income *= 0.75
rent = total_income * 0.10
final_income = total_income - rent

if final_income >= tour_price:
    print(f"Yes! {final_income - tour_price:.2f} lv left.")
else:
    print(f"Not enough money! {tour_price - final_income:.2f} lv needed.")
