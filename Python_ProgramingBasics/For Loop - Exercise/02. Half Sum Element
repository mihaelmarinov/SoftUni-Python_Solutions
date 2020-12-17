import sys

num = int(input())

top_num = -sys.maxsize
total_num = 0

for i in range(0, num):
    num1 = int(input())
    total_num += num1

    if num1 > top_num:
        top_num = num1


total_num = total_num - top_num

if total_num == top_num:
    print("Yes")
    print(f"Sum = {top_num}")
else:
    print("No")
    print(f"Diff = {abs(total_num - top_num)}")
