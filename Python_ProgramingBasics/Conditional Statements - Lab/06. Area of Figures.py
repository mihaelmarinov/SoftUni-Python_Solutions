figure_type = str(input())

if figure_type == "square":
    side = float(input())
    result = side * side
elif figure_type == "rectangle":
    sideA = float(input())
    sideB = float(input())
    result = sideA * sideB
elif figure_type == "circle":
    radius = float(input())
    from math import pi
    result = pi * (radius * radius)
elif figure_type == "triangle":
    base = float(input())
    height = float(input())
    result = (base * height) / 2

print(f"{result:.3f}")
