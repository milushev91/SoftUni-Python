# cook your dish here
PRICES = {
    "one": {
        "Small": 9.98,
        "Middle": 18.99,
        "Large": 25.98,
        "ExtraLarge": 35.99,
    },
    
    "two": {
        "Small": 8.58,
        "Middle": 17.09,
        "Large": 23.59,
        "ExtraLarge": 31.79,
    },
}

contract_duration = input()
contract_type = input()
has_mobile_internet = input()
months_count = int(input())

monthly_tax = PRICES[contract_duration][contract_type]

if has_mobile_internet == "yes":
    if monthly_tax <= 10:
        monthly_tax += 5.50
    elif monthly_tax <= 30:
        monthly_tax += 4.35
    else:
        monthly_tax += 3.85 

total_tax = monthly_tax * months_count

if contract_duration == "two":
    total_tax *= 0.9625

print(f"{total_tax:.2f} lv.")
    
    
    
