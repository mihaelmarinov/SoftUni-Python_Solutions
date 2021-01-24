from collections import deque

n = int(input())


gas_station = deque()

for i in range(n):
    p_d = list(map(int, input().split()))
    gas_station.append(p_d)

for f in range(len(gas_station)):
    flag = True
    cur_gas = 0
    for n in range(len(gas_station)):
        current_station = gas_station.popleft()
        gas, distance = current_station
        cur_gas += gas - distance

        if cur_gas < 0:
            flag = False
        gas_station.append(current_station)
    if flag:
        print(f)
        break
    gas_station.append(gas_station.popleft())
