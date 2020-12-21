cells = input().split("#")
water = int(input())

High = range(81, 126)
Medium = range(51, 81)
Low = range(1, 51)

total_fire = 0
effort = 0

valid_cells = []

def validity_checker(type, value):
    index = int(value)
    if type == "High":
        if index in High:
            valid_cells.append(index)
    elif type == "Medium":
        if index in Medium:
            valid_cells.append(index)
    elif type == "Low":
        if index in Low:
            valid_cells.append(index)

for cell in cells:
    cel = cell.split(" = ")
    validity_checker(cel[0],cel[1])

cells_out = []

for i in valid_cells:
    if water < 0:
        pass
    else:
        if water - i >= 0:
            water -= i
            total_fire += i
            effort += i * 0.25
            cells_out.append(i)
        else:
            pass

print("Cells:")
for j in cells_out:
    print(f' - {j}')
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
