book_searched = str(input())
search_book = str(input())

book_count = 0
is_the_right_book = False

while search_book != "No More Books":
    if book_searched == search_book:
        is_the_right_book = True
        print(f"You checked {book_count} books and found it.")
        break

    search_book = str(input())
    book_count += 1

if not is_the_right_book:
    print("The book you search is not here!")
    print(f"You checked {book_count} books.")
