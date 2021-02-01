def unique_names(num):
    names = []
    for _ in range(num):
        name = input()
        if name not in names:
            names.append(name)

    return set(names)


def names_printer(collection):
    for el in collection:
        print(el)


n = int(input())
names_printer(unique_names(n))
