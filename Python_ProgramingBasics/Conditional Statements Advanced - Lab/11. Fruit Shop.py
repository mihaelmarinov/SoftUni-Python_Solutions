fruit = input()
day_of_week = input()
quantity = float(input())

price = 0
product_options = ["banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes"]
workday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]

if day_of_week in workday and fruit in product_options:
    if fruit == "banana":
        price = 2.50
    elif fruit == "apple":
        price = 1.20
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.70
    elif fruit == "pineapple":
        price = 5.50
    elif fruit == "grapes":
        price = 3.85
elif day_of_week in weekend and fruit in product_options:
    if fruit == "banana":
        price = 2.70
    elif fruit == "apple":
        price = 1.25
    elif fruit == "orange":
        price = 0.90
    elif fruit == "grapefruit":
        price = 1.60
    elif fruit == "kiwi":
        price = 3.00
    elif fruit == "pineapple":
        price = 5.60
    elif fruit == "grapes":
        price = 4.20
else:
    print("error")

if fruit in product_options and day_of_week in workday:
    print(f"{price * quantity:.2f}")
if fruit in product_options and day_of_week in weekend:
    print(f"{price * quantity:.2f}")
