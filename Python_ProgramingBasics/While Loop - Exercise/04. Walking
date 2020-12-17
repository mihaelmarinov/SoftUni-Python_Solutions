command = input()

sum_steps = 0
goal_reached = False

while command != "Going home":
    done_steps = int(command)
    sum_steps += done_steps
    
    if sum_steps >= 10000:
        goal_reached = True
        print("Goal reached! Good job!")
        print(f"{sum_steps - 10000} steps over the goal!")
        break

    
    command = input()

if not goal_reached:
    steps_to_home = int(input())
    sum_steps += steps_to_home
    if sum_steps >= 10000:
        print("Goal reached! Good job!")
        print(f"{sum_steps - 10000} steps over the goal!")
    else:
        print(f"{abs(sum_steps - 10000)} more steps to reach goal.")
