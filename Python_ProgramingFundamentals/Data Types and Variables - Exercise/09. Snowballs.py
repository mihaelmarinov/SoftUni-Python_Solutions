n = int(input())

snowball_value = 0
best_snow = 0
best_time = 0
best_quality = 0

for i in range(1, n+1):
    snow = int(input())
    time = int(input())
    quality = int(input())

    value = (snow / time)** quality

    if value >= snowball_value:
        snowball_value = value
        best_snow = snow
        best_time = time
        best_quality = quality


print(f"{best_snow} : {best_time} = {int(snowball_value)} ({best_quality})")
