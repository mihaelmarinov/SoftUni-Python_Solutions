divisor = int(input())
bound = int(input())
n = 0

for i in range(1, bound + 1):
    if i <= bound:
        if i % divisor == 0:
            if i > n:
                n = i

print(n)
