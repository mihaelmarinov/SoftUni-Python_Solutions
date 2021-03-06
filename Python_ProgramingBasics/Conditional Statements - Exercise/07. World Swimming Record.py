import math

record_time = float(input())
distance = float(input())
time_per_m = float(input())

total_time = distance * time_per_m

friction_delay = math.floor(distance / 15) * 12.5

actual_time = total_time + friction_delay

if actual_time < record_time:
    print(f"Yes, he succeeded! The new world record is {actual_time:.2f} seconds.")
else:
    time_dif = actual_time - record_time
    print(f"No, he failed! He was {time_dif:.2f} seconds slower.")
