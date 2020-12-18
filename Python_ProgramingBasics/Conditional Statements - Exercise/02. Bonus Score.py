num_value = int(input())
bonus_points = 0

if num_value <= 100:
    bonus_points = 5
elif num_value > 1000:
    bonus_points = num_value * 0.10
else:
    bonus_points = num_value * 0.20

if num_value % 2 == 0:
    bonus_points = bonus_points + 1
elif num_value % 10 == 5:
    bonus_points = bonus_points + 2

print(bonus_points)
print(float(bonus_points + num_value))
