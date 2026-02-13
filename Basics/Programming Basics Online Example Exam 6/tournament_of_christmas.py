days = int(input())

earned_money = 0
wins = loses = 0
for _ in range(days):
    command = input()
    
    daily_wins = daily_loses = 0
    daiy_earnigs = 0
    while command != "Finish":
        sport = command
        outcome = input()
        
        if outcome == "win":
            daily_wins += 1 
            daiy_earnigs += 20
        else:
            daily_loses += 1
        
        command = input()
    
    if daily_wins > daily_loses:
        daiy_earnigs *= 1.10
    
    earned_money += daiy_earnigs
    wins += daily_wins
    loses += daily_loses

if wins > loses:
    earned_money *= 1.20
    print(f"You won the tournament! Total raised money: {earned_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {earned_money:.2f}")
