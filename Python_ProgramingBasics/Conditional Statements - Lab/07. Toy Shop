vacation_price = float(input())
puzzle_count = int(input())
doll_count = int(input())
bears_count = int(input())
minion_count = int(input())
trucks_count = int(input())

sold_toys_count = puzzle_count + doll_count + bears_count + minion_count + trucks_count
profit = (puzzle_count * 2.60) + (doll_count * 3) + (bears_count * 4.10) + (minion_count * 8.20) + (trucks_count * 2)

if sold_toys_count >= 50:
    profit = profit * 0.75

profit_after_rent = profit * 0.90
difference = abs(vacation_price - profit_after_rent)

if profit_after_rent >= vacation_price:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")
