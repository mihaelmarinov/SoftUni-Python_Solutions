from collections import deque

players = input().split()
steps = int(input())

q = deque(players)

# counter = 0
#
# while len(q) > 1:
#     counter += 1
#     current_player = q.popleft()
#     if counter == steps:
#         print(f"Removed {current_player}")
#         counter = 0
#     else:
#         q.append(current_player)

while len(q) > 1:
    for i in range(steps - 1):
        q.append(q.popleft())
    print(f'Removed {q.popleft()}')

print(f'Last is {q.popleft()}')
