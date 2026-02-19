# cook your dish here
PRICES = {
    "Ornament Set": {
        "Price": 2,
        "Points": 5,
    },
    
    "Tree Skirts": {
        "Price": 5,
        "Points": 3,
    },
    
    "Tree Garland": {
        "Price": 3,
        "Points": 10,
    },
    
    "Tree Lights": {
        "Price": 15,
        "Points": 17,
    },
}

quantity = int(input())
days = int(input())

budget = 0 
spirit = 0 

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    
    if day % 2 == 0:
        decoration_info = PRICES["Ornament Set"]
        budget += decoration_info["Price"] * quantity
        spirit += decoration_info["Points"]
    
    if day % 3 == 0:
        decoration1_info = PRICES["Tree Skirts"] 
        decoration2_info = PRICES["Tree Garland"] 
        budget += (decoration1_info["Price"] + decoration2_info["Price"]) * quantity
        spirit += decoration1_info["Points"] + decoration2_info["Points"] 
    
    if day % 5 == 0:
        decoration_info = PRICES["Tree Lights"]
        budget += decoration_info["Price"] * quantity
        spirit += decoration_info["Points"] 
        
        if day % 3 == 0:
            spirit += 30
    
    if day % 10 == 0:
        spirit -= 20
        decoration1_info = PRICES["Tree Skirts"]
        decoration2_info = PRICES["Tree Garland"] 
        decoration3_info = PRICES["Tree Lights"] 
        budget += decoration1_info["Price"] + decoration2_info["Price"] + decoration3_info["Price"]
        
    
    if day % 10 == 0 and day == days:
        spirit -= 30

    
print(f"Total cost: {budget}")
print(f"Total spirit: {spirit}")
