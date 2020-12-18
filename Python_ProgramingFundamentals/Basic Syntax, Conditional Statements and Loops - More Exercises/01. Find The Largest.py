from itertools import permutations

num = input()
numls = list(num)

def largest(l):
    lst = []
    for i in permutations(l, len(l)):
        lst.append("".join(map(str,i)))
    return max(lst)

print(largest(numls))
