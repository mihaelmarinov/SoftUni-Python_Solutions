gifts = input().split()
command = input().split()

def none_remover(gift):
    while "None" in gifts:
        gifts.remove("None")
    print(" ".join(gifts))

def out_of_stock(gift):
    for i in range(len(gifts)):
        if gifts[i] == gift:
            gifts[i] = "None"

def required(gift, index):
    if 0 <= index < len(gifts):
        gifts[index] = gift
    elif index == len(gifts):
        gifts[index - 1] = gift

def just_in_case(gift):
    num = len(gifts) - 1
    gifts[num] = gift


while "No" and "Money" not in command:
    if "OutOfStock" in command:
        out_of_stock(command[1])
    elif "Required" in command:
        required(command[1], int(command[2]))
    elif "JustInCase" in command:
        just_in_case(command[1])

    command = input().split()

none_remover(gifts)
