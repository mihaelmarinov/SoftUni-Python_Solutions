budget = float(input())
price_flour = float(input())

price_eggs = 0.75 * price_flour
price_milk = 0.25 * (1.25 * price_flour)

price_per_one = price_eggs + price_flour + price_milk
cozonac_count = 0
colored_eggs = 0

while budget > price_per_one:
    budget -= price_per_one
    cozonac_count += 1
    colored_eggs += 3
    if cozonac_count % 3 == 0:
        colored_eggs -= cozonac_count - 2


print(f"You made {cozonac_count} cozonacs! Now you have {colored_eggs} eggs"
      f" and {budget:.2f}BGN left.")
