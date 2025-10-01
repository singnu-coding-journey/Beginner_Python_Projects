def check_prime(num):
    if num < 2:
        print(f"{num} is not a prime number.")
        return

    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            return
    print(f"{num} is a prime number.")

num = int(input("Enter the number: "))

check_prime(num)

