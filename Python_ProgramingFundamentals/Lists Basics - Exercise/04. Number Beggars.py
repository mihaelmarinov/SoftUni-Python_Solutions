numbers = input().split(',')
beggars = int(input())

beggars_list = [[] for beggar in range(beggars)]

while len(numbers) != 0:
    for i in range(beggars):
        beggars_list[i].append(numbers[0])
        numbers.remove(numbers[0])
        if len(numbers) == 0:
            break


sum_of_beggars = []

for j in range(len(beggars_list)):
    sum_of_beggars.append(sum(int(el) for el in beggars_list[j]))

print(sum_of_beggars)
