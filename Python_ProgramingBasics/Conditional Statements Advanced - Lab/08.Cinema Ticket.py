day_of_week = str(input())

cheep_ticket_days = ["Monday", "Tuesday", "Friday"]
averg_ticket_days = ["Wednesday", "Thursday"]
expens_ticket_days = ["Saturday", "Sunday"]

if day_of_week in cheep_ticket_days:
    print("12")
elif day_of_week in averg_ticket_days:
    print("14")
elif day_of_week in expens_ticket_days:
    print("16")
