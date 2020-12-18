import sys

n = int(input())

max_num = -sys.maxsize
min_num = sys.maxsize

for i in range(n):
    n1 = int(input())

    if n1 > max_num:
        max_num = n1
    if n1 < min_num:
        min_num = n1


print(f"Max number: {max_num}")
print(f"Min number: {min_num}")
