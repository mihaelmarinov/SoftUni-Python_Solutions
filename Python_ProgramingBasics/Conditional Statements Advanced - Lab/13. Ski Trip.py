number_of_days = int(input())
type_of_room = input()
opinion = input()

number_of_nights = number_of_days - 1
price_for_night = 0
discount_price = 0
final_price = 0
total_price = 0

if type_of_room == "room for one person":
    price_for_night = 18.00
    final_price = number_of_nights * price_for_night
elif type_of_room == "apartment":
    price_for_night = 25.00
    final_price = number_of_nights * price_for_night
    if number_of_nights < 10:
        discount_price = final_price * 0.30
    elif 10 <= number_of_nights <= 15:
        discount_price = final_price * 0.35
    else:
        discount_price = final_price * 0.50
elif type_of_room == "president apartment":
    price_for_night = 35.00
    final_price = number_of_nights * price_for_night
    if number_of_nights < 10:
        discount_price = final_price * 0.10
    elif 10 <= number_of_nights <= 15:
        discount_price = final_price * 0.15
    else:
        discount_price = final_price * 0.20


total_price = final_price - discount_price

if opinion == "positive":
    total_price = total_price + (total_price * 0.25)
elif opinion == "negative":
    total_price = total_price - (total_price * 0.10)

print(f"{total_price:.2f}")
