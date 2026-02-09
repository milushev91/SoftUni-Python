# cook your dish here
budget = float(input())

command = input()

while command != "ACTION":
    name = command
    pay = budget * 0.20
    
    if len(name) <= 15:
        pay = float(input())
        
    budget -= pay
    
    if budget < 0:
        print(f"We need {abs(budget):.2f} leva for our actors.")
        break
    
    command = input()
else:
    print(f"We are left with {budget:.2f} leva.")
    
        
