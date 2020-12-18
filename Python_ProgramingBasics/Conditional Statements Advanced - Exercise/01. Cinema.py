movie_type = str(input())
r = int(input())
c = int(input())
ful_capacity = 0

if movie_type == "Premiere":
    ful_capacity = (r * c) * 12
elif movie_type == "Normal":
    ful_capacity = (r * c) * 7.50
elif movie_type == "Discount":
    ful_capacity = (r * c) * 5

print(f"{ful_capacity:.2f} leva")
