def periodic_table(n):
    elements = []

    for _ in range(n):
        element = input().split()
        for _ in element:
            elements.append(_)

    return set(elements)


n = int(input())

for el in periodic_table(n):
    print(el)
