numbers = input().split()

stack = []

for num in range(len(numbers)):
    stack.append(numbers.pop())

print(" ".join(stack))
