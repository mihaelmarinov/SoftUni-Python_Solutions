width = int(input())
length = int(input())

area = width * length

command = input()
sum_pieces = 0

while command != "STOP":
    piece = int(command)
    sum_pieces += piece

    if sum_pieces >= area:
        print(f"No more cake left! You need {sum_pieces - area} pieces more.")
        break

    command = input()

if command == "STOP":
    print(f"{area - sum_pieces} pieces are left.")
