camp_Days = int(input())
bakers_Count = int(input())
cake_Count = int(input())
gofreti_count = int(input())
crapes_count = int(input())
cakeAmount = cake_Count * 45
gofretiAmount = gofreti_count * 5.80
crapesAmount = crapes_count * 3.20
full_amountA =  camp_Days * (bakers_Count * (cakeAmount + gofretiAmount + crapesAmount))
full_amountB = full_amountA - (full_amountA * 0.125)
print(full_amountB)
