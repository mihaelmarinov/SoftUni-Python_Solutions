p = int(input())
c = int(input())

runs = p // c
if p % c != 0:
    runs += 1

print(runs)
