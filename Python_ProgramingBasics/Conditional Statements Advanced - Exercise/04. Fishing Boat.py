group_budget = int(input())
season = str(input())
angler_count = int(input())

boat_price = 0
disc_boat_price = 0
even_count = angler_count % 2

if season == "Spring":
    boat_price = 3000
    if angler_count <= 6:
        disc_boat_price = boat_price * 0.9
    elif 7 < angler_count <= 11:
        disc_boat_price = boat_price * 0.85
    elif angler_count >= 12:
        disc_boat_price = boat_price * 0.75
elif season == "Summer":
    boat_price = 4200
    if angler_count <= 6:
        disc_boat_price = boat_price * 0.90
    elif 7 < angler_count <= 11:
        disc_boat_price = boat_price * 0.85
    elif angler_count >= 12:
        disc_boat_price = boat_price * 0.75
elif season == "Autumn":
    boat_price = 4200
    if angler_count <= 6:
        disc_boat_price = boat_price * 0.90
    elif 7 < angler_count <= 11:
        disc_boat_price = boat_price * 0.85
    elif angler_count >= 12:
        disc_boat_price = boat_price * 0.75
elif season == "Winter":
    boat_price = 2600
    if angler_count <= 6:
        disc_boat_price = boat_price * 0.9
    elif 7 < angler_count <= 11:
        disc_boat_price = boat_price * 0.85
    elif angler_count >= 12:
        disc_boat_price = boat_price * 0.75

if even_count == 0 and season != "Autumn":
    disc_boat_price = disc_boat_price * 0.95

if group_budget >= disc_boat_price:
    print(f"Yes! You have {group_budget - disc_boat_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(group_budget - disc_boat_price):.2f} leva.")
