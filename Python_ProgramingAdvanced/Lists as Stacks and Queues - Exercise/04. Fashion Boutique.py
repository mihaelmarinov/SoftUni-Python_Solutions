clothes = list(map(int, input().split()))
capacity = int(input())
summary = 0
racks = []

while clothes:
    price = clothes.pop()
    summary += price
    if summary > capacity:
        clothes.append(price)
        racks.append(summary - price)
        summary = 0
    elif summary == capacity:
        racks.append(summary)
        summary = 0

if summary != 0:
    racks.append(summary)
    summary = 0

print(len(racks))
