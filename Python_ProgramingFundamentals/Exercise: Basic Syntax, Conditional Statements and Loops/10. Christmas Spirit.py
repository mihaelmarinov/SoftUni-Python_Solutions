quantity = int(input())
days = int(input())

ornament_set = 2
tree_skirt = 5
garlands_tree = 3
tree_lights = 15

total_spirit = 0
total_cost = 0

for i in range(1, days + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        total_cost += ornament_set * quantity
        total_spirit += 5
    if i % 3 == 0:
        total_cost += tree_skirt * quantity
        total_cost += garlands_tree * quantity
        total_spirit += 13
    if i % 5 == 0:
        total_cost += tree_lights * quantity
        total_spirit += 17
        if i % 3 == 0:
            total_spirit += 30
    if i % 10 == 0:
        total_cost += tree_skirt + garlands_tree + tree_lights
        total_spirit -= 20

if days % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
