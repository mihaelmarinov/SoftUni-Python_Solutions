budget_amount = float(input())
movie_extras = int(input())
price_clothing = float(input())

budget_amount = budget_amount * 0.90

if movie_extras > 150:
    price_clothing = price_clothing * 0.90

total_price = movie_extras * price_clothing

if total_price > budget_amount:
    money_difference = total_price - budget_amount
    print("Not enough money!")
    print(f"Wingard needs {money_difference:.2f} leva more.")
else:
    money_difference = budget_amount - total_price
    print("Action!")
    print(f"Wingard starts filming with {money_difference:.2f} leva left.")
