month = input()
length_of_stay = int(input())

studio = 0
apartment = 0
total_price_studio = 0
total_price_apart = 0

if month == "May" or month == "October":
    studio = 50
    apartment = 65
    total_price_studio = length_of_stay * studio
    total_price_apart = length_of_stay * apartment
    if 7 < length_of_stay < 14:
        total_price_studio = total_price_studio * 0.95
    elif 14 < length_of_stay:
        total_price_studio = total_price_studio * 0.70
elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    total_price_studio = length_of_stay * studio
    total_price_apart = length_of_stay * apartment
    if 14 < length_of_stay:
        total_price_studio = total_price_studio * 0.80
elif month == "July" or month == "August":
    studio = 76
    apartment = 77
    total_price_studio = length_of_stay * studio
    total_price_apart = length_of_stay * apartment

if 14 < length_of_stay:
    total_price_apart = total_price_apart * 0.90

print(f"Apartment: {total_price_apart:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")
