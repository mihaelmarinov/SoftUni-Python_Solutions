numbers = input().split()
n = int(input())

num_converted = [int(num) for num in numbers]

for i in range(n):
    num_converted.remove(min(num_converted))


print(num_converted)
