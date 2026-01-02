city = input()
income = float(input())

commission_percent = 0

if city == "Sofia":
    if 0 <= income <= 500:
        commission_percent = 0.05
    elif 500 < income <= 1000:
        commission_percent = 0.07
    elif 1000 < income <= 10000:
        commission_percent = 0.08
    elif income > 10000:
        commission_percent = 0.12
    else:
        print("error")
elif city == "Varna":
    if 0 <= income <= 500:
        commission_percent = 0.045
    elif 500 < income <= 1000:
        commission_percent = 0.075
    elif 1000 < income <= 10000:
        commission_percent = 0.10
    elif income > 10000:
        commission_percent = 0.13
    else:
        print("error")
elif city == "Plovdiv":
    if 0 <= income <= 500:
        commission_percent = 0.055
    elif 500 < income <= 1000:
        commission_percent = 0.08
    elif 1000 < income <= 10000:
        commission_percent = 0.12
    elif income > 10000:
        commission_percent = 0.145
    else:
        print("error")
else:
    print("error")

if commission_percent != 0:
    commission = income * commission_percent
    print(f"{commission:.2f}")
