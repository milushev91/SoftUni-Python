# cook your dish here
DELIVERY_PRICE = 60

joints_count = int(input())
joints_type = input()
has_delivery = input()

if joints_count <= 10:
    print("Invalid order")
else:
    joint_price = 0 

    if joints_type == "90X130":
        joint_price = 110 
        
        if joints_count > 60:
            joint_price *= 0.92
        elif joints_count > 30:
            joint_price *= 0.95 
    
    elif joints_type == "100X150":
        joint_price = 140

        if joints_count > 80:
            joint_price *= 0.90
        elif joints_count > 40:
            joint_price *= 0.94

    elif joints_type == "130X180":
        joint_price = 190

        if joints_count > 50:
            joint_price *= 0.88
        elif joints_count > 20:
            joint_price *= 0.93   
    
    elif joints_type == "200X300":
        joint_price = 210

        if joints_count > 50:
            joint_price *= 0.86
        elif joints_count > 25:
            joint_price *= 0.91 
    
    total_price = joint_price * joints_count
    
    if has_delivery == "With delivery":
        total_price += DELIVERY_PRICE
    
    if joints_count > 99:
        total_price *= 0.96
    
    print(f"{total_price:.2f} BGN")
