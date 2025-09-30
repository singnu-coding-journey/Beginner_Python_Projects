def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiple(a, b):
    return a * b

def divide(a, b):
    return a / b  

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter hte second number: "))

print("Sum:", add(number1, number2))
print("Difference:", subtract(number1, number2))
print("product: ", multiple(number1, number2))
print("Quotient: ", divide(number1, number2))