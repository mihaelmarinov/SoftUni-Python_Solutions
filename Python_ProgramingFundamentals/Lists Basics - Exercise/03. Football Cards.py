team_A = [a for a in range(1, 12)]
team_B = [b for b in range(1, 12)]


cards = input().split()
len_el = 0

for el in cards:
    len_el += 1


    elem = el.split('-')
    if elem[0] == "A":
        if int(elem[1]) in team_A:
            team_A.remove(int(elem[1]))
        else:
            pass
    elif elem[0] == "B":
        if int(elem[1]) in team_B:
            team_B.remove(int(elem[1]))
        else:
            pass


    if len(team_A) < 7:
        print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
        print("Game was terminated")
        break
    elif len(team_A) < 7:
        print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
        print("Game was terminated")
        break

    if len_el == len(cards):
        print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
