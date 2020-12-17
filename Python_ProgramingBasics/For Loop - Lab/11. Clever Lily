n = int(input())
laundry = float(input())
p = int(input())

money_even = 0
money_odd = 0
even = 0
odd = 0

for i in range(1, n+1):
    if i % 2 != 0:
        odd += 1
        money_odd = p * odd
    if i % 2 == 0:
        even += 1
        money_even += (10 * even)

total_money = (money_even + money_odd) - even

if total_money >= laundry:
    print(f"Yes! {abs(laundry - total_money):.2f}")
else:
    print(f"No! {abs(total_money - laundry):.2f}")
