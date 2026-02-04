# cook your dish here
movies_count = int(input())

lowest_rating = float("inf")
highest_rating = float("-inf")
lowest_name = highest_name = ""
total_rating = 0

for _ in range(movies_count):
    movie_name = input()
    rating = float(input())
    
    total_rating += rating
    
    if rating < lowest_rating:
        lowest_rating = rating
        lowest_name = movie_name
    
    if highest_rating < rating:
        highest_rating = rating
        highest_name = movie_name

print(f"{highest_name} is with highest rating: {highest_rating}")
print(f"{lowest_name} is with lowest rating: {lowest_rating}")
print(f"Average rating: {total_rating / movies_count:.1f}")

    
