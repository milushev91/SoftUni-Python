# cook your dish here

PRICES = {
    "withEquipment": [100, 0.1],
    "noEquipment": [80, 0.05],
    "withBreakfast": [130, 0.12],
    "noBreakfast": [130, 0.07],
}

VALID_INPUT = ["Bansko", "Borovets", "Varna", "Burgas", "noEquipment", "withEquipment", "withBreakfast", "noBreakfast" ]

city_name = input()
package = input()
vip_discount = input()
days = int(input())

if city_name not in VALID_INPUT or package not in VALID_INPUT:

    print("Invalid input!")
elif days < 1:
    print("Days must be positive number!")
else:
    price, discount = PRICES[package]
    
    if days > 7:
        days -= 1
    
    if vip_discount == "yes":
        price -= price * discount
    
    final_price = days * price
    print(f"The price is {final_price:.2f}lv! Have a nice time!")
