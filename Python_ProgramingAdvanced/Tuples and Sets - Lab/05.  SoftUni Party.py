def input_to_list(num):
    lines = []
    for _ in range(num):
        lines.append(input())

    return lines


def is_vip_guest(guest):
    return guest[0].isdigit()


def guest_separator(guest):
    vip_guests = []
    regular_guests = []
    for guest in guest:
        if is_vip_guest(guest):
            vip_guests.append(guest)
        else:
            regular_guests.append(guest)
    return sorted(vip_guests), sorted(regular_guests)


def print_result(guests):
    (vip_guests, regular_guests) = guest_separator(guests)

    for guest in vip_guests:
        print(guest)

    for guest in regular_guests:
        print(guest)


reservation = input_to_list(int(input()))
arrived = []

while True:
    command = input()
    if command == "END":
        break
    else:
        arrived.append(command)


not_arrived = set(reservation).difference(arrived)

print(len(not_arrived))
print_result(not_arrived)