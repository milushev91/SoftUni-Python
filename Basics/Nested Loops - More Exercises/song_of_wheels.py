control_number = int(input())
counter = 0
password = ""
found_password = False

for a in range(1, 10):
    for b in range(1, 10):
        #a < b 

        for c in range(1, 10):
            if a >= b:
                break
            
            for d in range(1, 10):
                #c > d
                if d >= c:
                    break
                
                if a * b + c * d != control_number:
                    continue
                    
                counter += 1
                print(f"{a}{b}{c}{d}", end=" ")
                
                if counter == 4:
                    password = f"{a}{b}{c}{d}"
                    found_password = True
print()                   
if found_password:
    print(f"Password: {password}")
else:
    print("No!")
                    
                
