PRICES = {
    "John Wick": {
        "Drink": 12,
        "Popcorn": 15,
        "Menu": 19,
    },
    "Star Wars": {
        "Drink": 18,
        "Popcorn": 25,
        "Menu": 30,
    },
    "Jumanji": {
        "Drink": 9,
        "Popcorn": 11,
        "Menu": 14,
    },
}

movie = input()
package = input()
tickets_count = int(input())

price = PRICES[movie][package]

if movie == "Star Wars" and tickets_count >= 4:
    price *= 0.70
elif movie == "Jumanji" and tickets_count == 2:
    price *= 0.85
    
final_price = price * tickets_count

print(f"Your bill is {final_price:.2f} leva.")
    
