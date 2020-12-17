open_tabs = int(input())
salary = float(input())

f = 0
insta = 0
r = 0

for i in range(0, open_tabs):
    site_name = str(input())

    if site_name == "Facebook":
        f += 1
    elif site_name == "Instagram":
        insta += 1
    elif site_name == "Reddit":
        r += 1

penalty = (f * 150) + (insta * 100) + (r * 50)
money_left = salary - penalty

if money_left <= 0:
    print("You have lost your salary.")
else:
    print(int(money_left))
