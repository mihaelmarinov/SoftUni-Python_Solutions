factor = int(input())
count = int(input())

multiple = []

for i in range(1, count + 1):
    number = i * factor
    multiple.append(number)


print(multiple)
