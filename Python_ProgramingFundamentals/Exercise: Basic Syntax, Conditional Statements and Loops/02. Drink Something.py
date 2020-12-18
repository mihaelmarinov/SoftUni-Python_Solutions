age = int(input())

def drink_something(years):
    if years <= 14:
        return "drink toddy"
    elif years <= 18:
        return "drink coke"
    elif years <= 21:
        return "drink beer"
    elif years > 21:
        return "drink whisky"


print(drink_something(age))
