hours = int(input())
minutes = int(input())


new_time = (hours * 60 + minutes) + 15
minutes = new_time % 60
new_time = new_time // 60

if minutes > 59:
    hours = new_time + 1
else:
    hours = new_time


if hours > 23:
    hours = 0

if minutes < 10:
    print(f'{hours}:0{minutes}')
else:
    print(f'{hours}:{minutes}')
