start = int(input())
end = int(input())
magic_num = int(input())

is_found = False
num_count = 0

for i in range(start, end + 1):
    if is_found:
        break
    for x in range(start, end + 1):
        num_count += 1
        if i + x == magic_num:
            is_found = True
            print(f"Combination N:{num_count} ({i} + {x} = {magic_num})")
            break
if not is_found:
    print(f"{num_count} combinations - neither equals {magic_num}")
