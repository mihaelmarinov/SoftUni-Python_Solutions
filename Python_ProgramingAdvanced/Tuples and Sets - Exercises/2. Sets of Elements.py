n, m = map(int, input().split())


def set_comparison(num1, num2):
    n_set = []
    m_set = []

    for _ in range(num1):
        n_set.append(input())

    for _ in range(num2):
        m_set.append(input())

    unique_values = set(n_set) & set(m_set)

    return unique_values


for el in set_comparison(n, m):
    print(el)