# Marin and Nelly are buying a house not far from Sofia. Nelly loves flowers so much that she convinces you to write a program that calculates
# how much it will cost them to plant a certain number of flowers and whether the available budget will be enough.

type_flowers = str(input())
count_flower = int(input())
budget = int(input())

price_per_flower = 0

if type_flowers == "Roses":
    price_per_flower = 5
elif type_flowers == "Dahlias":
    price_per_flower = 3.80
elif type_flowers == "Tulips":
    price_per_flower = 2.80
elif type_flowers == "Narcissus":
    price_per_flower = 3
elif type_flowers == "Gladiolus":
    price_per_flower = 2.50

total_price = count_flower * price_per_flower

if count_flower > 80 and type_flowers == "Roses":
    total_price = total_price * 0.90
elif count_flower > 90 and type_flowers == "Dahlias":
    total_price = total_price * 0.85
elif count_flower > 80 and type_flowers == "Tulips":
    total_price = total_price * 0.85
elif count_flower < 120 and type_flowers == "Narcissus":
    total_price = total_price * 1.15
elif count_flower < 80 and type_flowers == "Gladiolus":
    total_price = total_price * 1.20

if budget >= total_price:
    print(f"Hey, you have a great garden with {count_flower} {type_flowers} and {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(budget - total_price):.2f} leva more.")
