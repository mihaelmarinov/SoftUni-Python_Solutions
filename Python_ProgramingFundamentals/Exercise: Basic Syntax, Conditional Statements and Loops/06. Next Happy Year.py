year = int(input())
year += 1

while True:
    if len(str(year)) != len(set(str(year))):
        year += 1
    else:
        print(int(year))
        break
