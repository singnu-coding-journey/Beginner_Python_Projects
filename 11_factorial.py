def factorial_function(num):
    total = 1
    for i in range(num, 0, -1):
        total = total * i
    print(f"The factorial of {num} is {total}")    
        


num = int(input("Enter the number: "))

factorial_function(num)