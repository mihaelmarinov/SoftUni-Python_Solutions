def longest_intersection(n):
    long_inter = []
    for _ in range(n):

        first, second = input().split("-")
        first_start, first_end = map(int, first.split(","))
        second_start, second_end = map(int, second.split(","))

        first = []
        second = []

        for i in range(first_start, first_end + 1):
            first.append(i)

        for x in range(second_start, second_end + 1):
            second.append(x)

        inter = set(first) & set(second)

        if len(long_inter) < len(inter):
            long_inter = list(inter)

    print(f'Longest intersection is {long_inter} with length {len(long_inter)}')


longest_intersection(int(input()))