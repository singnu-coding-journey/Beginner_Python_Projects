import math

def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.\n")

def calculator():
    print("Welcome to the safe calculator!")
    print("Available operations:")
    print(" + Add")
    print(" - Subtract")
    print(" * Multiple")
    print(" / Divide")
    print(" ^ Power")
    print(" √ Square root")
    print("Type 'q' to quit.\n")

    while True:
        operator = input("Choose an operator (+, -, *, /, ^, √) or 'q' to quit: ").strip()

        if operator.lower() == 'q':
            print("Goodbye!")
            break 
        if operator == '√':
            num = get_number("Enter the number to find the square roof of: ")
            if num < 0:
                print("Error: Cannot take the square root of a negative number.\n")
                continue
            result = math.sqrt(num)
            print(f"Result: √{num} = {result}")
            continue


        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            try:
                result = num1 / num2
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.\n")
                continue
        elif operator == '^':
            result = math.pow(num1, num2)
        else:
            print("Invalid operator. Please choose a valid one.\n")
        print(f"Result: {num1} {operator} {num2 if operator != '√' else ''} = {result}\n") 


calculator()        



