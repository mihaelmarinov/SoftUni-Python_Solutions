number = float(input())
value1 = str(input())
value2 = str(input())
result = 0

if value1 == "m" and value2 == "cm":
    result = number * 100
elif value1 == "m" and value2 == "mm":
    result = number  * 1000
elif value1 == "cm" and value2 == "m":
    result = number / 100
elif value1 == "cm" and value2 == "mm":
    result = number * 10
elif value1 == "mm" and value2 == "m":
    result = number / 1000
elif value1 == "mm" and value2 == "cm":
    result = number / 10

result = "{:.3f}".format(result)
print(result)
