n = int(input())

parking = set()


for i in range(n):
    direction, car_number = input().split(", ")

    if direction == 'IN':
        parking.add(car_number)
    elif direction == "OUT":
        parking.remove(car_number)

if len(parking) == 0:
    print('Parking Lot is Empty')
else:
    for el in parking:
        print(el)