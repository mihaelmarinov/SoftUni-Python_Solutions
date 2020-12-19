n = int(input())

sum = 0

for i in range(n):
    sym = input()
    sum += ord(sym)


print(f'The sum equals: {sum}')
