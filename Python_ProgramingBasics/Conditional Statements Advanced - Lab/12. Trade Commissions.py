city = str(input())
sales_volume = float(input())
commission = 0

sal_num = sales_volume > 0
city_option = ["Sofia", "Plovdiv", "Varna"]

if city == "Sofia" and sal_num is True:
    if 0 <= sales_volume <= 500:
        commission = 0.05
    elif 500 <= sales_volume <= 1000:
        commission = 0.07
    elif 1000 <= sales_volume <= 10000:
        commission = 0.08
    else:
        commission = 0.12
elif city == "Varna" and sal_num is True:
    if 0 <= sales_volume <= 500:
        commission = 0.045
    elif 500 <= sales_volume <= 1000:
        commission = 0.075
    elif 1000 <= sales_volume <= 10000:
        commission = 0.10
    else:
        commission = 0.13
elif city == "Plovdiv" and sal_num is True:
    if 0 <= sales_volume <= 500:
        commission = 0.055
    elif 500 <= sales_volume <= 1000:
        commission = 0.08
    elif 1000 <= sales_volume <= 10000:
        commission = 0.12
    else:
        commission = 0.145
elif sal_num is False:
    print("error")
else:
    print("error")

if city in city_option and sal_num is True:
    print(f'{sales_volume * commission:.2f}')
