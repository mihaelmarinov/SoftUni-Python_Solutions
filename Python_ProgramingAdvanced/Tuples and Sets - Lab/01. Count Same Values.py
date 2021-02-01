
# values_count = {}
#
# for value in values:
#     if value not in values_count:
#         values_count[value] = 0
#     values_count[value] += 1

values = list(map(float, input().split()))

values_count = {}

for value in values:
    values_count[value] = values.count(value)

for key, val in values_count.items():
    print(f'{key} - {val} times')
