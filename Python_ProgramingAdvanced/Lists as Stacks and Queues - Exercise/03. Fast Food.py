from collections import deque

food = int(input())
orders = deque(list(map(int, input().split())))
max_order = max(orders)

while orders:
    order = orders.popleft()

    if order > food:
        orders.appendleft(order)
        break
    food -= order

print(max_order)
if orders:
    print(f"Orders left:", end=" ")
    print(*orders)
else:
    print("Orders complete")
