vacation_money = float(input())
saved_money = float(input())

count_days = 0
spend_days = 0

while vacation_money > saved_money and spend_days < 5:
    day_type = str(input())
    money = float(input())

    count_days += 1
    if day_type == "save":
        saved_money += money
        spend_days = 0
    elif day_type == "spend":
        spend_days += 1
        saved_money -= money
        if saved_money < 0:
            saved_money = 0

    if spend_days == 5:
        print("You can't save the money.")
        print(count_days)
        break
    if saved_money >= vacation_money:
        print(f"You saved the money for {count_days} days.")
        break
