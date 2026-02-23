# cook your dish here
n = int(input())

first_bracket = ""

for _ in range(n):
    line = input()
    
    if line not in "()":
        continue
    
    if line == "(" and not first_bracket:
        first_bracket = "("
    elif line == ")" and first_bracket:
        first_bracket = ""
    else:
        print("UNBALANCED")
        break

else:
    print("BALANCED")
    
    
        
    
    
        
    
    
    
    


