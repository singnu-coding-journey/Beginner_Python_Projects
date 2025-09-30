import math

def area(r):
    return math.pi * r ** 2


def perimeter(r):
    return 2 * math.pi * r


r = float(input("Enter the radius of the circle: "))

a = area(r)
p = perimeter(r)

print(f"Area of the circle: {a}")
print(f"Perimeter of the circle: {p}")
