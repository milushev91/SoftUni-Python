capacity = int(input())
fans_count = int(input())

a_sector = 0
b_sector = 0
v_sector = 0
g_sector = 0
 
for _ in range(fans_count):
    sector = input()
    
    if sector == "A":
        a_sector += 1 
    elif sector == "B":
        b_sector += 1 
    elif sector == "V":
        v_sector += 1 
    else:
        g_sector += 1 

for sector in [a_sector, b_sector, v_sector, g_sector]:
    print(f"{sector / fans_count * 100:.2f}%")
    
fans_percent = fans_count / capacity * 100

print(f"{fans_percent:.2f}%")

