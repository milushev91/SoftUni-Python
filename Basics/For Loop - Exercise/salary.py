tabs = int(input())
salary = int(input())

penalties = {
    "Facebook": 150,
    "Instagram": 100,
	  "Reddit": 50,
}

for _ in range(tabs):
    site = input()
    
    if site not in penalties:
        continue
    
    salary -= penalties[site]
    
    if salary <= 0:
        print("You have lost your salary.")
        break 
else:
    print(int(salary))
