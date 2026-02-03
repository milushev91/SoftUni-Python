TICKET_PRICES = {
    "A Star Is Born": {
        "normal": 7.50,
        "luxury": 10.50,
        "ultra luxury": 13.50,
    },
    "Bohemian Rhapsody": {
        "normal": 7.35,
        "luxury": 9.45,
        "ultra luxury": 12.75,
    },
    "Green Book": {
        "normal": 8.15,
        "luxury": 10.25,
        "ultra luxury": 13.25,
    },
    "The Favourite": {
        "normal": 8.75,
        "luxury": 11.55,
        "ultra luxury": 13.95,
    }
}

movie = input()
hall_type = input()
tickets_count = int(input())

cinema_income = tickets_count * TICKET_PRICES[movie][hall_type]
print(f"{movie} -> {cinema_income:.2f} lv.")
