country = input()
instrument = input()

difficulty = performance = 0

if instrument == "ribbon":
    if country == "Russia":
        difficulty = 9.100
        performance = 9.400
    elif country == "Bulgaria":
        difficulty = 9.600
        performance = 9.400
    elif country == "Italy":
        difficulty = 9.200
        performance = 9.500
elif instrument == "hoop":
    if country == "Russia":
        difficulty = 9.300
        performance = 9.800
    elif country == "Bulgaria":
        difficulty = 9.550
        performance = 9.750
    elif country == "Italy":
        difficulty = 9.450
        performance = 9.350
elif instrument == "rope":
    if country == "Russia":
        difficulty = 9.600
        performance = 9.000
    elif country == "Bulgaria":
        difficulty = 9.500
        performance = 9.400
    elif country == "Italy":
        difficulty = 9.700
        performance = 9.150

total_grade = difficulty + performance
print(f"The team of {country} get {total_grade:.3f} on {instrument}.")
print(f"{abs(total_grade / 20 * 100 - 100):.2f}%")
