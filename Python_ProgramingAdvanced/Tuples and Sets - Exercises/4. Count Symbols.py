def count_symbols(text):
    unique_values = set(text)

    for char in sorted(unique_values):
        print(f'{char}: {text.count(char)} time/s')


count_symbols(list(input()))