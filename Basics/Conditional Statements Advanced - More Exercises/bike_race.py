juniors_count = int(input())
seniors_count = int(input())
trace = input()

junior_tax = senior_tax = 0
 
if trace == "trail":
    junior_tax = 5.50
    senior_tax = 7
    
elif trace == "cross-country":
    junior_tax = 8 
    senior_tax = 9.50
    
    if juniors_count + seniors_count >= 50:
        junior_tax *= 0.75
        senior_tax *= 0.75
    
elif trace == "downhill":
    junior_tax = 12.25
    senior_tax = 13.75
    
else:
    junior_tax = 20 
    senior_tax = 21.50

income = juniors_count * junior_tax + seniors_count * senior_tax
costs = income * 0.05
final_sum = income - costs

print("{:.2f}".format(final_sum))
