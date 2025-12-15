deposited_amount = float(input())
deposit_term = int(input())
anual_interest_percent = float(input())

monthly_interest_pecent = (anual_interest_percent / 100) / 12
interest_amount = (monthly_interest_pecent * deposited_amount) * deposit_term
final_amount = deposited_amount + interest_amount

print(final_amount)
