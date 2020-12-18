exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_in_minutes = (exam_hour * 60) + exam_minutes
arrival_in_minutes = (arrival_hour * 60) + arrival_minutes
differ_early = exam_in_minutes - arrival_in_minutes
differ_late = arrival_in_minutes - exam_in_minutes

if exam_in_minutes - 30 <= arrival_in_minutes <= exam_in_minutes:
    print("On time")
    if exam_in_minutes != arrival_in_minutes:
        differ = exam_in_minutes - arrival_in_minutes
        print(f"{differ} minutes before the start")
elif arrival_in_minutes < exam_in_minutes - 30:
    print("Early")
    if differ_early < 60:
        print(f"{differ_early} minutes before the start")
    else:
        differ_hour = differ_early // 60
        differ_mins = differ_early % 60
        if differ_mins < 10:
            print(f"{differ_hour}:0{differ_mins} hours before the start")
        else:
            print(f"{differ_hour}:{differ_mins} hours before the start")
else:
    print("Late")
    if differ_late < 60:
        print(f"{abs(differ_late)} minutes after the start")
    else:
        differ_hour = differ_late // 60
        differ_mins = differ_late % 60
        if differ_mins < 10:
            print(f"{differ_hour}:0{differ_mins} hours after the start")
        else:
            print(f"{differ_hour}:{differ_mins} hours after the start")
