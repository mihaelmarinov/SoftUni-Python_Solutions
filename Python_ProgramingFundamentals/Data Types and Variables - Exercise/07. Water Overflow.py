n = int(input())

capacity = 255
litter_in = 0

for i in range(n):
    water = int(input())
    capacity -= water
    if capacity < 0:
        print("Insufficient capacity!")
        capacity += water
        continue
    else:
        litter_in += water

print(litter_in)
