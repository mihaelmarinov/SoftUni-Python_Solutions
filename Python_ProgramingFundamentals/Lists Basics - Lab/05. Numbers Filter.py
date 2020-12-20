n = int(input())

even = []
odd = []
negative = []
positive = []

for i in range(n):
    num = int(input())
    if num % 2 == 0:
        even.append(num)
        if num >= 0:
            positive.append(num)
        else:
            negative.append(num)
    else:
        odd.append(num)
        if num >= 0:
            positive.append(num)
        else:
            negative.append(num)

command = input()

if command == "even":
    print(even)
elif command == "odd":
    print(odd)
elif command == "negative":
    print(negative)
elif command == "positive":
    print(positive)
