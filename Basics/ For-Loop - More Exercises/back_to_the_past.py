START_YEAR = 1800
SPENT_MONEY = 12000

inhereted_money = float(input())
year_to_live = int(input())

age = 18
spent_money = 0

for year in range(START_YEAR, year_to_live + 1):

    spent_money += 12000

    if year % 2 != 0:
        spent_money += 50 * age 
    
    age += 1

difference = f"{abs(inhereted_money - spent_money):.2f}"

if inhereted_money >= spent_money:
    print(f"Yes! He will live a carefree life and will have {difference} dollars left.")
else:
    print(f"He will need {difference} dollars to survive.")
