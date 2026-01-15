book_name = input()
command = input()

book_counter = 0

while command != "No More Books":
    current_book = command
     
    
    if current_book == book_name:
        print(f"You checked {book_counter} books and found it.")
        break
    book_counter += 1
    
    command = input()
else:
    print("The book you search is not here!")
    print(f"You checked {book_counter} books.")
