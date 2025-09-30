def largest_of_three_number(a, b, c):
    if a > b and a > c:
        print("a is the largest")
    elif b > a and b > c:
        print("b is the largest")
    else:
        print("c is the largest")

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

largest_of_three_number(a, b, c)
