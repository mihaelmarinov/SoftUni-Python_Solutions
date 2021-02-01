def name_value(name, line):
    name_list = list(name)

    name_prize = 0

    for el in name_list:
        name_prize += ord(el)

    value = int(name_prize / line)

    return value


even = set()
odd = set()

n = int(input())

for i in range(1, n + 1):
    name = input()
    prize = name_value(name, i)

    if prize % 2 == 0:
        even.add(prize)
    else:
        odd.add(prize)


if sum(odd) == sum(even):
    print(', '.join(map(str, odd & even)))
elif sum(odd) > sum(even):
    print(', '.join(map(str, odd - even)))
elif sum(odd) < sum(even):
    print(', '.join(map(str, odd ^ even)))