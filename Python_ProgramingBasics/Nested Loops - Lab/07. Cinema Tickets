movie_name = str(input())

total_tickets = 0
sold_tickets = 0
student_tickets = 0
standard_tickets = 0
kids_tickets = 0

while movie_name != "Finish":
    free_space = int(input())
    sold_tickets = 0

    ticket_type = input()

    while ticket_type != "End":
        sold_tickets += 1
        total_tickets += 1
        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kids_tickets += 1

        if sold_tickets == free_space:
            break
        ticket_type = input()

    print(f"{movie_name} - {(sold_tickets/ free_space) * 100:.2f}% full.")

    movie_name = str(input())

print(f"Total tickets: {total_tickets}")
print(f"{(student_tickets / total_tickets) * 100:.2f}% student tickets.")
print(f"{(standard_tickets / total_tickets) * 100:.2f}% standard tickets.")
print(f"{(kids_tickets / total_tickets) * 100:.2f}% kids tickets.")
