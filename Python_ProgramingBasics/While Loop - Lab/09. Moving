width = int(input())
length = int(input())
height = int(input())
box_num = input()

apartment_volume = width * length * height
occupied_volume = 0

while box_num != "Done":
    box_volume = int(box_num)

    occupied_volume += box_volume

    if occupied_volume >= apartment_volume:
        print(f"No more free space! You need {occupied_volume - apartment_volume} Cubic meters more.")
        break

    box_num = input()

if box_num == "Done":
    print(f"{apartment_volume - occupied_volume} Cubic meters left.")
