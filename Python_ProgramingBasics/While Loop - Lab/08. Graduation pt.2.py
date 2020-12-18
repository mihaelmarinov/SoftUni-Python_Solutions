name = input()

year = 1
bad_grades = 0
total_grades = 0

while year <= 12:
    grade = float(input())

    if grade < 4:
        bad_grades += 1

        if bad_grades == 2:
            break
        continue

    total_grades += grade

    year += 1

if bad_grades == 2:
    print(f"{name} has been excluded at {year} grade")
else:
    year -= 1
    print(f"{name} graduated. Average grade: {total_grades / year:.2f}")
