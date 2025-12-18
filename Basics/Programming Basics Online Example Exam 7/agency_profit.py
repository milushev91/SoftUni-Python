company_name = input()
adult_tickets_count = int(input())
child_tickets_count = int(input())
adult_ticket_price = float(input())
ticket_tax = float(input())

adult_tickets = (adult_ticket_price + ticket_tax) * adult_tickets_count
child_tickets_price = (adult_ticket_price * 0.30 + ticket_tax) * child_tickets_count

income = adult_tickets + child_tickets_price
profit = income * 0.20

print(f"The profit of your agency from {company_name} tickets is {profit:.2f} lv.")
