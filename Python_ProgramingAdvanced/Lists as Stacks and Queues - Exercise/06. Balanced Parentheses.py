parentheses = list(input())
is_balanced = True

balanced = []
pairs = {'(':')', '{':'}', '[':']'}

for el in parentheses:
    if el in "({[":
        balanced.append(el)
    else:
        if not balanced:
            is_balanced = False
            break
        current_open = balanced.pop()
        if not el == pairs[current_open]:
            is_balanced = False
            break

if is_balanced:
    print('YES')
else:
    print('NO')
