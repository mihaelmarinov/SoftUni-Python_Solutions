failed_max = int(input())

sum_grades = 0
num_tasks = 0
name_last_task = " "
failed_grades = 0


while failed_grades < failed_max:
    name_task = str(input())
    if name_task == "Enough":
        print(f"Average score: {sum_grades / num_tasks:.2f}")
        print(f"Number of problems: {num_tasks}")
        print(f"Last problem: {name_last_task}")
        break

    grade = int(input())

    if grade <= 4:
        failed_grades += 1
        if failed_grades == failed_max:
            print(f"You need a break, {failed_grades} poor grades.")
            break

    num_tasks += 1
    name_last_task = name_task
    sum_grades += grade
