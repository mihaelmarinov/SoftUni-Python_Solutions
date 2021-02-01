n = int(input())

names_grades = {}

for i in range(n):
    name, grade = input().split()
    if name not in names_grades:
        names_grades[name] = ["{:.2f}".format(float(grade))]
    else:
        names_grades[name].append("{:.2f}".format(float(grade)))

for n, g in names_grades.items():
    print(f'{n} -> {" ".join(g)} (avg: {sum(map(float, g)) / len(g):.2f})')