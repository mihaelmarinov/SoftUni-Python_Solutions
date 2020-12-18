n = int(input())
presentation = input()

final_assessment = 0
exam_times = 0

while presentation != "Finish":
    average_per_presentation = 0

    for i in range(1, n + 1):
        grade = float(input())
        average_per_presentation += grade

    exam_times += 1
    average_per_presentation /= n
    final_assessment += average_per_presentation

    print(f"{presentation} - {average_per_presentation:.2f}.")

    presentation = input()

print(f"Student's final assessment is {final_assessment / exam_times:.2f}.")
