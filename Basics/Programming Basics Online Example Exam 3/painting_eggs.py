PRICES = {
    "Large": {
        "Red": 16,
        "Green": 12,
        "Yellow": 9,
    },
    "Medium":  {
        "Red": 13,
        "Green": 9,
        "Yellow": 7,
    },
    "Small":  {
        "Red": 9,
        "Green": 8,
        "Yellow": 5,
    },
}

size = input()
color = input()
quantity = int(input())

income = PRICES[size][color] * quantity
expenses = income * 0.35
final_income = income - expenses

print(f"{final_income:.2f} leva.")
