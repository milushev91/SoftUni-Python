movie_name = input()
days = int(input())
tickets_count = int(input())
ticket_price = float(input())
cinema_share_percent = int(input()) / 100 

total_tickets = days * tickets_count
income = total_tickets * ticket_price
cinema_share = income * cinema_share_percent

final_income = income - cinema_share

print(f"The profit from the movie {movie_name} is {final_income:.2f} lv.")
