first_string = input()
second_string = input()

current_string = ""
pre_string = first_string

for i in range(len(first_string)):
    for m in range(0, i + 1):
        current_string += second_string[m]
    for k in range(i+ 1, len(first_string)):
        current_string += first_string[k]

    if not pre_string == current_string:
        print(current_string)
    pre_string = current_string
    current_string = ""
