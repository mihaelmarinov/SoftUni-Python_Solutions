budget = float(input())
season = str(input())

vacation_money = 0
destination = 0
vacation_type = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        vacation_type = "Camp"
        vacation_money = budget * 0.30
    elif season == "winter":
        vacation_type = "Hotel"
        vacation_money = budget * 0.70
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        vacation_type = "Camp"
        vacation_money = budget * 0.40
    elif season == "winter":
        vacation_type = "Hotel"
        vacation_money = budget * 0.80
else:
    destination = "Europe"
    vacation_type = "Hotel"
    vacation_money = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{vacation_type} - {vacation_money:.2f}")
