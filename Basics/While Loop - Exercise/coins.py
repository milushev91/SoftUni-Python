amount = int(float(input()) * 100)

coins_count = 0 

while amount > 0:
    coin = 0 
    
    if amount >= 200:
        coin = 200
    elif amount >= 100:
        coin = 100 
    elif amount >= 50:
        coin = 50 
    elif amount >= 20:
        coin = 20
    elif amount >= 10:
        coin = 10
    elif amount >= 5:
        coin = 5 
    elif amount >= 2:
        coin = 2
    elif amount >= 1:
        coin = 1 
    
    coins_count += 1 
    amount -= coin

print(coins_count)
