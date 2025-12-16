anual_tax = int(input())

sneakers = anual_tax - anual_tax * 0.40
outfit = sneakers - sneakers * 0.20
ball = outfit / 4 
accessories = ball / 5 

total_price = anual_tax + sneakers + outfit + ball + accessories

print(total_price)
