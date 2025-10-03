def fibonacci(n):
    a, b = 0, 1
    sequence = []  
    for i in range(n):
        sequence.append(a)
        temp = a + b
        a = b
        b = temp   
    print(sequence)


fibonacci(10)          
